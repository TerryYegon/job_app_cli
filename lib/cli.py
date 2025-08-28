from models.job import Job
from models.application import Application
from helpers import exit_program, input_int

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_job()
        elif choice == "2":
            list_jobs()
        elif choice == "3":
            delete_job()
        elif choice == "4":
            create_application()
        elif choice == "5":
            list_applications()
        elif choice == "6":
            delete_application()
        elif choice == "7":
            view_applications_for_job()
        else:
            print("Invalid choice")

def menu():
    print("\nPlease select an option:")
    print("0. Exit the program")
    print("1. Create a Job")
    print("2. List all Jobs")
    print("3. Delete a Job")
    print("4. Create an Application")
    print("5. List all Applications")
    print("6. Delete an Application")
    print("7. View Applications for a Job")

def create_job():
    title = input("Job Title: ")
    description = input("Job Description: ")
    try:
        Job.create(title, description)
        print("Job created!")
    except Exception as e:
        print(f"Error: {e}")

def list_jobs():
    jobs = Job.get_all()
    for job in jobs:
        print(f"ID: {job.id} | Title: {job.title} | Description: {job.description}")

def delete_job():
    job_id = input_int("Enter Job ID to delete: ")
    Job.delete(job_id)
    print("Job deleted (if it existed).")

def create_application():
    job_id = input_int("Job ID to apply for: ")
    applicant_name = input("Applicant Name: ")
    email = input("Applicant Email: ")
    try:
        Application.create(job_id, applicant_name, email)
        print("Application created!")
    except Exception as e:
        print(f"Error: {e}")

def list_applications():
    apps = Application.get_all()
    for app in apps:
        print(f"ID: {app.id} | Job ID: {app.job_id} | Name: {app.applicant_name} | Email: {app.email}")

def delete_application():
    app_id = input_int("Enter Application ID to delete: ")
    Application.delete(app_id)
    print("Application deleted (if it existed).")

def view_applications_for_job():
    job_id = input_int("Enter Job ID: ")
    apps = Application.get_by_job(job_id)
    if not apps:
        print("No applications for this job.")
    for app in apps:
        print(f"ID: {app.id} | Name: {app.applicant_name} | Email: {app.email}")

if __name__ == "__main__":
    main()
