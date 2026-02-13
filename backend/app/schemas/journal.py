from datetime import datetime

from pydantic import BaseModel


class JournalCreate(BaseModel):
    title: str
    content: str
    mood_tag: str | None = None


class JournalResponse(BaseModel):
    id: int
    title: str
    content: str
    mood_tag: str | None
    created_at: datetime

    model_config = {"from_attributes": True}
