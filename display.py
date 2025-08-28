import json
from typing import Dict, List
from datetime import datetime

def print_header(title: str, width: int = 50):
    """Print a formatted header"""
    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width)

def print_separator(width: int = 50):
    """Print a separator line"""
    print("-" * width)

def display_applicant_summary(applicant: Dict):
    """Display applicant information in summary format"""
    print(f"\n{'='*60}")
    print(f" ID: {applicant['id']:>3} |  Status: {applicant['status']}")
    print(f" Name: {applicant['name']}")
    print(f" Email: {applicant['email']}")
    print(f" Phone: {applicant['phone']}")
    print(f" Position: {applicant['position']}")
    print(f" Experience: {applicant['experience']} years")
    
    # Handle skills display
    try:
        skills = json.loads(applicant['skills'])
        skills_str = ', '.join(skills)
    except (json.JSONDecodeError, TypeError):
        skills_str = applicant['skills'] or 'No skills listed'
    
    print(f"  Skills: {skills_str}")
    print(f" Applied: {format_date(applicant['application_date'])}")
    print(f"{'='*60}")

def display_applicant_detailed(applicant: Dict):
    """Display applicant information in detailed format"""
    print(f"\n{'='*70}")
    print(f"DETAILED APPLICATION VIEW - ID: {applicant['id']}")
    print(f"{'='*70}")
    
    print(f" PERSONAL INFORMATION")
    print_separator(30)
    print(f"Name: {applicant['name']}")
    print(f"Email: {applicant['email']}")
    print(f"Phone: {applicant['phone']}")
    
    print(f"\n JOB INFORMATION")
    print_separator(30)
    print(f"Position: {applicant['position']}")
    print(f"Experience: {applicant['experience']} years")
    print(f"Status: {applicant['status']}")
    print(f"Applied: {format_date(applicant['application_date'])}")
    
    # Handle skills display
    try:
        skills = json.loads(applicant['skills'])
        print(f"Skills:")
        for i, skill in enumerate(skills, 1):
            print(f"  {i}. {skill}")
    except (json.JSONDecodeError, TypeError):
        print(f"Skills: {applicant['skills'] or 'No skills listed'}")
    
    # Resume/Cover letter
    if applicant['resume_text'] and applicant['resume_text'].strip():
        print(f"\n RESUME/COVER LETTER")
        print_separator(30)
        print(applicant['resume_text'])
    else:
        print(f"\n RESUME/COVER LETTER: Not provided")
    
    print(f"{'='*70}")

def display_application_list(applicants: List[Dict], title: str = "Applications"):
    """Display a list of applications"""
    if not applicants:
        print(f"\n No {title.lower()} found.")
        return
    
    print_header(f"{title.upper()} ({len(applicants)} found)")
    
    for applicant in applicants:
        display_applicant_summary(applicant)
    
    print(f"\n Total: {len(applicants)} applications")

def display_menu(title: str, options: List[str]):
    """Display a menu with options"""
    print_header(title)
    
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    print()

def display_statistics(stats: Dict):
    """Display application statistics"""
    print_header("APPLICATION STATISTICS")
    
    print(f" Total Applications: {stats['total']}")
    
    if stats['status_breakdown']:
        print(f"\n Status Breakdown:")
        print_separator(25)
        for status, count in stats['status_breakdown'].items():
            percentage = (count / stats['total'] * 100) if stats['total'] > 0 else 0
            print(f"  {status}: {count} ({percentage:.1f}%)")
    
    print()

def format_date(date_string: str) -> str:
    """Format date string to readable format"""
    try:
        # Parse the SQLite datetime format
        dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        return dt.strftime("%Y-%m-%d %H:%M")
    except:
        return date_string

def display_success_message(message: str):
    """Display success message with formatting"""
    print(f"\n {message}")

def display_error_message(message: str):
    """Display error message with formatting"""
    print(f"\n {message}")

def display_info_message(message: str):
    """Display info message with formatting"""
    print(f"\n {message}")

def display_warning_message(message: str):
    """Display warning message with formatting"""
    print(f"\n  {message}")

def get_user_choice(prompt: str, valid_choices: List[str]) -> str:
    """Get validated user choice"""
    while True:
        choice = input(f"{prompt} ({'/'.join(valid_choices)}): ").strip().lower()
        if choice in valid_choices:
            return choice
        display_error_message(f"Invalid choice. Please select from: {', '.join(valid_choices)}")

def confirm_action(action: str) -> bool:
    """Get confirmation for an action"""
    response = get_user_choice(f"Are you sure you want to {action}?", ['y', 'n', 'yes', 'no'])
    return response in ['y', 'yes']

def display_welcome():
    """Display welcome message"""
    print("\n" + "="*60)
    print(" JOB APPLICATION MANAGEMENT SYSTEM")
    print("="*60)
    print("Welcome! Manage job applications efficiently.")
    print("Choose your role to get started.")
    print("="*60)

def print_application_summary(full_name, email, phone, position, years_exp, skills, resume):
    print(f" Name: {full_name}")
    print(f" Email: {email}")
    print(f" Phone: {phone}")
    print(f" Position: {position}")
    print(f" Experience: {years_exp} years")
    print(f"  Skills: {', '.join(skills)}")
    if resume:
        print(f" Resume: Provided ({len(resume)} characters)")
    else:
        print(" Resume: Not provided")