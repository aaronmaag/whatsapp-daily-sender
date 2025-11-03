from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column
from sqlalchemy import Integer, Text, Boolean, Date, ForeignKey, TIMESTAMP, text

Base = declarative_base()

class PhoneNumber(Base):
    __tablename__ = "phone_numbers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    phone_e164: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[str] = mapped_column(TIMESTAMP(timezone=True), server_default=text("NOW()"))
    updated_at: Mapped[str] = mapped_column(TIMESTAMP(timezone=True), server_default=text("NOW()"))

class DailyMessageLog(Base):
    __tablename__ = "daily_message_log"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    phone_id: Mapped[int] = mapped_column(ForeignKey("phone_numbers.id", ondelete="CASCADE"), nullable=False)
    template_name: Mapped[str] = mapped_column(Text, nullable=False)
    send_date: Mapped[str] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(Text, nullable=False)
    provider_message_id: Mapped[str | None] = mapped_column(Text, nullable=True)
    error_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[str] = mapped_column(TIMESTAMP(timezone=True), server_default=text("NOW()"))
