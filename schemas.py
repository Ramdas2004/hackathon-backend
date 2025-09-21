from pydantic import BaseModel

class ParticipantCreate(BaseModel):
    name: str
    skill: str
    experience: int

class ParticipantOut(ParticipantCreate):
    id: int