from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Application(Base):
    __tablename__ = 'applications'
    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey('jobs.id'))
    applicant_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    job = relationship('Job', back_populates='applications')

from .job import Job
Job.applications = relationship('Application', order_by=Application.id, back_populates='job')
