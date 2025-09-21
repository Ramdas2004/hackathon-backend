from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/participants/", response_model=schemas.ParticipantOut)
def create_participant(participant: schemas.ParticipantCreate, db: Session = Depends(get_db)):
    return crud.create_participant(db, participant)

@app.get("/participants/", response_model=list[schemas.ParticipantOut])
def get_participants(db: Session = Depends(get_db)):
    return crud.get_all_participants(db)