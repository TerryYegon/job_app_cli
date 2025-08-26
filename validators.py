import re
from typing import List

def validate_email(email: str) -> bool:
    """
    Validate email format
    Returns True if email is valid, False otherwise
    """
    if not email or not isinstance(email, str):
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_valid = re.match(pattern, email.strip()) is not None
    
    if not is_valid:
        print(" Invalid email format. Example: user@example.com")
    
    return is_valid

def validate_phone(phone: str) -> bool:
    """
    Validate phone number format
    Accepts various formats: +1234567890, (123) 456-7890, 123-456-7890, etc.
    """
    if not phone or not isinstance(phone, str):
        return False
    
    # Remove all non-digit characters except +
    clean_phone = re.sub(r'[^\d+]', '', phone.strip())
    
    # Check if it has reasonable length (7-15 digits, possibly with + prefix)
    pattern = r'^(\+)?\d{7,15}$'
    is_valid = re.match(pattern, clean_phone) is not None
    
    if not is_valid:
        print("Invalid phone format. Examples: +1234567890, (123) 456-7890, 123-456-7890")
    
    return is_valid

def validate_name(name: str) -> bool:
    """
    Validate name - should not be empty and contain only letters, spaces, hyphens, apostrophes
    """
    if not name or not isinstance(name, str):
        print(" Name cannot be empty")
        return False
    
    name = name.strip()
    if len(name) < 2:
        print(" Name must be at least 2 characters long")
        return False
    
    # Allow letters, spaces, hyphens, apostrophes
    pattern = r"^[a-zA-Z\s\-']+$"
    is_valid = re.match(pattern, name) is not None
    
    if not is_valid:
        print(" Name can only contain letters, spaces, hyphens, and apostrophes")
    
    return is_valid

def validate_position(position: str) -> bool:
    """
    Validate job position - should not be empty
    """
    if not position or not isinstance(position, str):
        print(" Position cannot be empty")
        return False
    
    position = position.strip()
    if len(position) < 2:
        print(" Position must be at least 2 characters long")
        return False
    
    return True

def validate_skills(skills: List[str]) -> bool:
    """
    Validate skills list - should have at least one non-empty skill
    """
    if not skills or not isinstance(skills, list):
        print(" At least one skill is required")
        return False
    
    valid_skills = [skill.strip() for skill in skills if skill.strip()]
    
    if not valid_skills:
        print(" At least one valid skill is required")
        return False
    
    return True

def validate_experience(experience: str) -> tuple[bool, int]:
    """
    Validate years of experience - should be a non-negative integer
    Returns (is_valid, experience_value)
    """
    try:
        exp_value = int(experience.strip())
        if exp_value < 0:
            print(" Experience cannot be negative")
            return False, 0
        if exp_value > 70:
            print("Experience seems unusually high. Please verify.")
            return False, 0
        return True, exp_value
    except ValueError:
        print(" Experience must be a valid number")
        return False, 0

def get_validated_input(prompt: str, validator_func, **kwargs):
    """
    Generic function to get validated input from user
    Keeps asking until valid input is provided
    """
    while True:
        user_input = input(prompt).strip()
        
        if validator_func == validate_experience:
            is_valid, value = validator_func(user_input)
            if is_valid:
                return value
        else:
            if validator_func(user_input, **kwargs):
                return user_input
        
        print("Please try again.\n")