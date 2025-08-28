import re
from display import print_application_summary
from db import save_application_record
from validators import validate_email, validate_phone

def submit_application():
    print("\n" + "=" * 50)
    print("SUBMIT JOB APPLICATION")
    print(" Please fill out all required information")
    print(" PERSONAL INFORMATION")
    full_name = input("Full Name: ").strip()
    while not full_name:
        print("Name is required.")
        full_name = input("Full Name: ").strip()

    email = input("Email Address: ").strip()
    while not validate_email(email):
        print("Invalid or missing email address.")
        email = input("Email Address: ").strip()

    phone = input("Phone Number: ").strip()
    while not validate_phone(phone):
        print("Invalid or missing phone number.")
        phone = input("Phone Number: ").strip()

    print(" JOB INFORMATION")
    position = input("Position Applied For: ").strip()
    while not position:
        print("Position is required.")
        position = input("Position Applied For: ").strip()

    print("Enter your skills separated by commas:")
    print("Examples: Python, SQL, Project Management, Communication")
    skills_raw = input("Skills: ").strip()
    skills = [s.strip() for s in skills_raw.split(',') if s.strip()]
    print(f"Parsed skills: {', '.join(skills)}")
    confirm = input("Are these skills correct? (y/n): ").strip().lower()
    if confirm != 'y':
        return submit_application()

    years_exp = input("Years of Experience: ").strip()
    while not years_exp.isdigit():
        print("Please enter a valid number.")
        years_exp = input("Years of Experience: ").strip()
    years_exp = int(years_exp)

    print(" RESUME/COVER LETTER")
    print("Enter your resume/cover letter (optional):")
    print("You can paste multiple lines. Press Enter twice when finished.")
    lines = []
    while True:
        line = input()
        if line == '':
            if lines:
                break
            else:
                continue
        lines.append(line)
    resume = '\n'.join(lines)
    resume_len = len(resume)
    if resume:
        print(f"Resume/Cover letter captured ({resume_len} characters)")
    else:
        print("No resume/cover letter provided.")

    print("=" * 50)
    print("APPLICATION SUMMARY")
    print_application_summary(full_name, email, phone, position, years_exp, skills, resume)
    confirm = input("Submit this application? (y/n): ").strip().lower()
    if confirm == 'y':
        save_application_record(full_name, email, phone, position, years_exp, skills, resume)
        print(f"✅ Application submitted successfully!\nℹ️  Thank you, {full_name}! We'll review your application and get back to you soon.")
    else:
        print("Application not submitted.")
