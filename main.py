from db import JobApplicationDB
from validators import validate_email, validate_phone, validate_name
from display import display_welcome, display_menu, display_success_message
if __name__ == "__main__":
    db = JobApplicationDB()   # this initializes the DB and creates the tables

    # Validators
    print("Testing Validators:")
    print("Email test:", validate_email("user@example.com"))
    print("Phone test:", validate_phone("+1234567890"))
    print("Name test:", validate_name("John Doe"))

    # Display
    display_welcome()
    display_menu("Main Menu", ["Add Applicant", "View Applicants", "Exit"])
    display_success_message("Applicant added successfully!")
