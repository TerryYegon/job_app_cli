import sys
from applicant import submit_application
#from hr_admin import hr_portal  # Uncomment and implement as needed
#from migrations import migration_tools  # Uncomment and implement as needed

def main_menu():
    while True:
        print("\n JOB APPLICATION MANAGEMENT SYSTEM")
        print("Welcome! Manage job applications efficiently.")
        print("Choose your role to get started.")
        print("=" * 50)
        print("MAIN MENU\n")
        print("1. Applicant Portal - Submit Applications")
        print("2. HR/Admin Portal - Manage Applications")
        print("3. Database Migration Tools")
        print("4. Exit System\n")
        choice = input("Select option (1-4): ").strip()
        if choice == '1':
            applicant_portal()
        elif choice == '2':
            print("\n[HR/Admin Portal coming soon]")
            #hr_portal()
        elif choice == '3':
            print("\n[Migration Tools coming soon]")
            #migration_tools()
        elif choice == '4':
            print("Exiting system. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option. Please select 1-4.")

def applicant_portal():
    while True:
        print("\n" + "=" * 50)
        print("APPLICANT PORTAL\n")
        print("1. Submit New Application")
        print("2. Back to Main Menu")
        print("3. Exit System\n")
        choice = input("Select option (1-3): ").strip()
        if choice == '1':
            submit_application()
        elif choice == '2':
            return
        elif choice == '3':
            print("Exiting system. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option. Please select 1-3.")

if __name__ == "__main__":
    main_menu()
