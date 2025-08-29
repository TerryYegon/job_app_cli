import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.models.job import Job
from lib.models.application import Application
from lib.helpers import exit_program, input_int, get_session
import subprocess

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            applicant_portal()
        elif choice == "2":
            hr_admin_portal()
        elif choice == "3":
            migration_tools_menu()
        else:
            print("Invalid choice")

def menu():
    print("\nJOB APPLICATION MANAGEMENT SYSTEM")
    print("Welcome! Manage job applications efficiently.")
    print("Choose your role to get started.")
    print("=" * 50)
    print("MAIN MENU\n")
    print("0. Exit the program")
    print("1. Applicant Portal - Submit Applications")
    print("2. HR/Admin Portal - Manage Applications")
    print("3. Database Migration Tools")

def applicant_portal():
    while True:
        print("\nAPPLICANT PORTAL\n")
        print("1. Create an Application")
        print("2. Back to Main Menu")
        choice = input("> ")
        if choice == "1":
            create_application()
        elif choice == "2":
            return
        else:
            print("Invalid choice")

def hr_admin_portal():
    while True:
        print("\nHR/ADMIN PORTAL\n")
        # Example of dict usage in the project
        hr_menu_options = {
            "1": "List all Jobs",
            "2": "List all Applications",
            "3": "View Applications for a Job",
            "4": "Add Job",
            "5": "Delete a Job",
            "6": "Delete an Application",
            "7": "Find Job by ID",
            "8": "Find Application by ID",
            "9": "Back to Main Menu"
        }
        for key, desc in hr_menu_options.items():
            print(f"{key}. {desc}")
        choice = input("> ")
        if choice == "1":
            list_jobs()
        elif choice == "2":
            list_applications()
        elif choice == "3":
            view_applications_for_job()
        elif choice == "4":
            create_job()
        elif choice == "5":
            delete_job()
        elif choice == "6":
            delete_application()
        elif choice == "7":
            find_job_by_id()
        elif choice == "8":
            find_application_by_id()
        elif choice == "9":
            return
        else:
            print("Invalid choice")

def migration_tools_menu():
    while True:
        print("\nDATABASE MIGRATION TOOLS\n")
        print("1. Show migration status")
        print("2. Apply migrations (upgrade)")
        print("3. Rollback last migration (downgrade)")
        print("4. Create new migration")
        print("5. Back to Main Menu")
        choice = input("> ")
        if choice == "1":
            run_alembic_command(["current"])
        elif choice == "2":
            run_alembic_command(["upgrade", "head"])
        elif choice == "3":
            run_alembic_command(["downgrade", "-1"])
        elif choice == "4":
            msg = input("Migration message: ")
            run_alembic_command(["revision", "--autogenerate", "-m", msg])
        elif choice == "5":
            return
        else:
            print("Invalid choice")

def run_alembic_command(args):
    # Example of list usage in the project: args is a list of command arguments
    try:
        result = subprocess.run(["alembic"] + args, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
    except Exception as e:
        print(f"Error running alembic: {e}")

def create_job():
    session = get_session()
    title = input("Job Title: ")
    description = input("Job Description: ")
    try:
        job = Job(title=title, description=description)
        session.add(job)
        session.commit()
        print("Job created!")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

def list_jobs():
    session = get_session()
    jobs = session.query(Job).all()
    for job in jobs:
        print(f"ID: {job.id} | Title: {job.title} | Description: {job.description}")
    session.close()

def delete_job():
    session = get_session()
    job_id = input_int("Enter Job ID to delete: ")
    job = session.query(Job).get(job_id)
    if job:
        session.delete(job)
        session.commit()
        print("Job deleted.")
    else:
        print("Job not found.")
    session.close()

def create_application():
    session = get_session()
    job_id = input_int("Job ID to apply for: ")
    applicant_name = input("Applicant Name: ")
    email = input("Applicant Email: ")
    try:
        app = Application(job_id=job_id, applicant_name=applicant_name, email=email)
        session.add(app)
        session.commit()
        print("Application created!")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

def list_applications():
    session = get_session()
    apps = session.query(Application).all()
    for app in apps:
        print(f"ID: {app.id} | Job ID: {app.job_id} | Name: {app.applicant_name} | Email: {app.email}")
    session.close()

def delete_application():
    session = get_session()
    app_id = input_int("Enter Application ID to delete: ")
    app = session.query(Application).get(app_id)
    if app:
        session.delete(app)
        session.commit()
        print("Application deleted.")
    else:
        print("Application not found.")
    session.close()

def view_applications_for_job():
    session = get_session()
    job_id = input_int("Enter Job ID: ")
    job = session.query(Job).get(job_id)
    if not job:
        print("Job not found.")
    else:
        apps = job.applications
        if not apps:
            print("No applications for this job.")
        for app in apps:
            print(f"ID: {app.id} | Name: {app.applicant_name} | Email: {app.email}")
    session.close()

def find_job_by_id():
    session = get_session()
    job_id = input_int("Enter Job ID: ")
    job = session.query(Job).get(job_id)
    if job:
        print(f"ID: {job.id} | Title: {job.title} | Description: {job.description}")
    else:
        print("Job not found.")
    session.close()

def find_application_by_id():
    session = get_session()
    app_id = input_int("Enter Application ID: ")
    app = session.query(Application).get(app_id)
    if app:
        print(f"ID: {app.id} | Job ID: {app.job_id} | Name: {app.applicant_name} | Email: {app.email}")
    else:
        print("Application not found.")
    session.close()

if __name__ == "__main__":
    main()
