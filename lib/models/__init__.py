# Models package init

from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .job import Job
from .application import Application
