from datetime import datetime

from sqlalchemy import Integer, Float, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class MoodEntry(Base):
    __tablename__ = "mood_entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    mood_score: Mapped[float] = mapped_column(Float, nullable=False)
    energy_level: Mapped[float] = mapped_column(Float, nullable=False)
    anxiety_level: Mapped[float] = mapped_column(Float, nullable=False)
    attachment_score: Mapped[float] = mapped_column(Float, nullable=True)
    label: Mapped[str] = mapped_column(String(50), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
