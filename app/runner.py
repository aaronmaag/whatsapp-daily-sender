import logging
import os
import json

from dotenv import load_dotenv

from app.db import engine
from app.models import Base
from app.sender import run_daily_send

# Create all tables if not exist
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))

    result = run_daily_send()
    print(json.dumps(result, indent=2))
