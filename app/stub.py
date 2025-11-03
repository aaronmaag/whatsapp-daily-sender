import uuid
import logging

log = logging.getLogger(__name__)

class WhatsAppStubClient:
    def send_template(self, phone_e164: str, template_name: str, params: dict | None = None) -> str:
        msg_id = f"stub-{uuid.uuid4()}"
        log.info(f"[STUB] Would send template '{template_name}' to {phone_e164} with params={params} -> {msg_id}")
        return msg_id
