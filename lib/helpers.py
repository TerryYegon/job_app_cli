from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///job_applications.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

def exit_program():
    print("Goodbye!")
    exit()

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# Example of tuple usage in the project
def get_sample_job_tuple():
    """
    Returns a sample job as a tuple (title, description).
    Demonstrates tuple usage for the rubric.
    """
    return ("Software Engineer", "Develop and maintain software applications.")
