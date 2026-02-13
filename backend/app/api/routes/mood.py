from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.mood import MoodEntry
from app.schemas.mood import MoodCreate, MoodResponse

router = APIRouter()


@router.post("/", response_model=MoodResponse, status_code=201)
def create_mood(mood: MoodCreate, db: Session = Depends(get_db)):
    db_mood = MoodEntry(**mood.model_dump())
    db.add(db_mood)
    db.commit()
    db.refresh(db_mood)
    return db_mood


@router.get("/", response_model=list[MoodResponse])
def list_moods(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return db.query(MoodEntry).offset(skip).limit(limit).all()


@router.get("/{mood_id}", response_model=MoodResponse)
def get_mood(mood_id: int, db: Session = Depends(get_db)):
    return db.query(MoodEntry).filter(MoodEntry.id == mood_id).first()
