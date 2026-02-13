from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.journal import JournalEntry
from app.schemas.journal import JournalCreate, JournalResponse

router = APIRouter()


@router.post("/", response_model=JournalResponse, status_code=201)
def create_journal(entry: JournalCreate, db: Session = Depends(get_db)):
    db_entry = JournalEntry(**entry.model_dump())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


@router.get("/", response_model=list[JournalResponse])
def list_journals(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return db.query(JournalEntry).offset(skip).limit(limit).all()


@router.get("/{journal_id}", response_model=JournalResponse)
def get_journal(journal_id: int, db: Session = Depends(get_db)):
    return db.query(JournalEntry).filter(JournalEntry.id == journal_id).first()
