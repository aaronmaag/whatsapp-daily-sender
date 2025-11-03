import logging, os, json
from dotenv import load_dotenv
from app.sender import run_daily_send

if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
    result = run_daily_send()
    print(json.dumps(result, indent=2))
