from sqlalchemy import Column, Integer, String
from . import Base

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    # Relationship is set in application.py
