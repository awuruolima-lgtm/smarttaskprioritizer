from sqlalchemy import Column, Integer, String, Float, Date
from .db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    urgency = Column(Integer, default=1)
    importance = Column(Integer, default=1)
    complexity = Column(Integer, default=1)
    category = Column(String, default="General")
    due_date = Column(Date, nullable=True)
    priority_score = Column(Float, default=0.0)
