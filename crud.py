from sqlalchemy.orm import Session
import models, schemas

def get_all_participants(db: Session):
    return db.query(models.Participant).all()

def create_participant(db: Session, participant: schemas.ParticipantCreate):
    db_participant = models.Participant(**participant.dict())
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant