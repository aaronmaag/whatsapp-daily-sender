import os
from datetime import datetime
import zoneinfo

def business_date_today() -> str:
    tz = zoneinfo.ZoneInfo(os.getenv("APP_TIMEZONE", "America/Toronto"))
    return datetime.now(tz).date().isoformat()
