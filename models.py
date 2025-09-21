from sqlalchemy import Column, Integer, String
from database import Base

class Participant(Base):
    __tablename__ = "participants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    skill = Column(String)
    experience = Column(Integer)