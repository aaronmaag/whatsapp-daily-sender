import os
from datetime import datetime
import zoneinfo
from datetime import date

def business_date_today() -> date:
    tz_name = os.getenv("APP_TIMEZONE", "America/Toronto").strip()
    tz = zoneinfo.ZoneInfo(tz_name)
    return datetime.now(tz).date()  # return date object, not string!
