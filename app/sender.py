import os
import logging
from sqlalchemy import select, insert
from app.db import SessionLocal
from app.models import PhoneNumber, DailyMessageLog
from app.stub import WhatsAppStubClient
from app.utils import business_date_today

log = logging.getLogger(__name__)

def run_daily_send(template_name: str | None = None, params: dict | None = None) -> dict:
    """
    Reads active phone numbers, sends at most once per business date.
    Returns a small summary dict for observability.
    """
    DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"
    template = template_name or os.getenv("DEFAULT_TEMPLATE_NAME", "daily_update_v1")
    today = business_date_today()

    sent = 0
    skipped = 0
    errors = 0

    client = WhatsAppStubClient()

    with SessionLocal() as db:
        numbers = db.scalars(select(PhoneNumber).where(PhoneNumber.active == True)).all()

        for p in numbers:
            # Check if we already sent today (unique constraint is the ultimate guard)
            already = db.scalar(
                select(DailyMessageLog).where(
                    DailyMessageLog.phone_id == p.id,
                    DailyMessageLog.template_name == template,
                    DailyMessageLog.send_date == today,
                )
            )
            if already:
                skipped += 1
                continue

            status = "DRY_RUN" if DRY_RUN else "SENT"
            provider_msg_id = None
            error_text = None

            try:
                if not DRY_RUN:
                    provider_msg_id = client.send_template(p.phone_e164, template, params)
                sent += 1
            except Exception as e:
                status = "ERROR"
                error_text = str(e)
                errors += 1
                log.exception(f"Error sending to {p.phone_e164}")

            # log the attempt (or the skip above is implicit—only log attempts)
            db.execute(
                insert(DailyMessageLog).values(
                    phone_id=p.id,
                    template_name=template,
                    send_date=today,
                    status=status if error_text is None else "ERROR",
                    provider_message_id=provider_msg_id,
                    error_text=error_text,
                )
            )
        db.commit()

    return {
    "date": today.isoformat(),
    "template": template,
    "sent": sent,
    "skipped": skipped,
    "errors": errors
}

