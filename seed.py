from app.db import SessionLocal
from app.models import PhoneNumber

def seed_numbers():
    db = SessionLocal()

    numbers = ["+16475551234", "+16135551234"]

    for num in numbers:
        exists = db.query(PhoneNumber).filter(PhoneNumber.phone_e164 == num).first()
        if not exists:
            db.add(PhoneNumber(phone_e164=num, active=True))
            print(f"Added {num}")

    db.commit()
    db.close()
    print("Seed complete.")

if __name__ == "__main__":
    seed_numbers()
