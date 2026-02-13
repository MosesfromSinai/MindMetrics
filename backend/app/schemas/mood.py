from datetime import datetime

from pydantic import BaseModel, Field


class MoodCreate(BaseModel):
    mood_score: float = Field(..., ge=0, le=10)
    energy_level: float = Field(..., ge=0, le=10)
    anxiety_level: float = Field(..., ge=0, le=10)
    attachment_score: float | None = Field(None, ge=0, le=10)
    label: str | None = None


class MoodResponse(BaseModel):
    id: int
    mood_score: float
    energy_level: float
    anxiety_level: float
    attachment_score: float | None
    label: str | None
    created_at: datetime

    model_config = {"from_attributes": True}
