import sqlite3
import json
from typing import List, Dict, Optional
from datetime import datetime

class JobApplicationDB:
    """Database handler for job applications"""
    
    def __init__(self, db_name: str = "job_applications.db"):
        self.db_name = db_name
        self.init_database()
        print(f" Database initialized: {db_name}")
    
    def init_database(self):
        """Initialize the database and create tables"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS applicants (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT,
                    position TEXT NOT NULL,
                    skills TEXT,
                    experience INTEGER,
                    resume_text TEXT,
                    application_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    status TEXT DEFAULT 'Pending'
                )
            ''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT,
                email TEXT,
                phone TEXT,
                position TEXT,
                years_exp INTEGER,
                skills TEXT,
                resume TEXT
            )''')
            conn.commit()
            print("Database tables 'applicants' and 'applications' ready")
    
    def add_applicant(self, name: str, email: str, phone: str, position: str, 
                     skills: List[str], experience: int, resume_text: str) -> bool:
        """Add a new applicant to the database"""
        try:
            skills_json = json.dumps(skills)
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO applicants (name, email, phone, position, skills, experience, resume_text)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (name, email, phone, position, skills_json, experience, resume_text))
                conn.commit()
                print(f" Added applicant: {name} ({email})")
                return True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
    
    def save_application(self, full_name: str, email: str, phone: str, position: str, 
                        years_exp: int, skills: List[str], resume: str) -> bool:
        """Save applicant data to the applications table"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO applications (full_name, email, phone, position, years_exp, skills, resume)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (full_name, email, phone, position, years_exp, json.dumps(skills), resume))
                conn.commit()
                print(f" Saved application for: {full_name} ({email})")
                return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
    
    def get_all_applicants(self) -> List[Dict]:
        """Get all applicants from the database"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM applicants ORDER BY application_date DESC')
            columns = [description[0] for description in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            print(f" Retrieved {len(result)} applications")
            return result
    
    def search_applicants(self, search_term: str, search_type: str) -> List[Dict]:
        """Search applicants by name, email, or position"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            if search_type == "name":
                cursor.execute('SELECT * FROM applicants WHERE name LIKE ?', (f'%{search_term}%',))
            elif search_type == "email":
                cursor.execute('SELECT * FROM applicants WHERE email LIKE ?', (f'%{search_term}%',))
            elif search_type == "position":
                cursor.execute('SELECT * FROM applicants WHERE position LIKE ?', (f'%{search_term}%',))
            
            columns = [description[0] for description in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]
            print(f"Found {len(result)} applications matching '{search_term}'")
            return result
    
    def filter_by_skill(self, skill: str) -> List[Dict]:
        """Filter applicants by a specific skill"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM applicants')
            columns = [description[0] for description in cursor.description]
            all_applicants = [dict(zip(columns, row)) for row in cursor.fetchall()]
            
            filtered = []
            for applicant in all_applicants:
                try:
                    skills = json.loads(applicant['skills'])
                    if any(skill.lower() in s.lower() for s in skills):
                        filtered.append(applicant)
                except (json.JSONDecodeError, TypeError):
                    # Handle legacy comma-separated skills
                    if applicant['skills'] and skill.lower() in applicant['skills'].lower():
                        filtered.append(applicant)
            
            print(f" Found {len(filtered)} applications with skill '{skill}'")
            return filtered
    
    def update_applicant_status(self, applicant_id: int, status: str) -> bool:
        """Update applicant status"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('UPDATE applicants SET status = ? WHERE id = ?', (status, applicant_id))
                conn.commit()
                success = cursor.rowcount > 0
                if success:
                    print(f" Updated applicant {applicant_id} status to '{status}'")
                else:
                    print(f" Applicant {applicant_id} not found")
                return success
        except sqlite3.Error as e:
            print(f" Database error: {e}")
            return False
    
    def delete_applicant(self, applicant_id: int) -> bool:
        """Delete an applicant from the database"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM applicants WHERE id = ?', (applicant_id,))
                conn.commit()
                success = cursor.rowcount > 0
                if success:
                    print(f" Deleted applicant {applicant_id}")
                else:
                    print(f" Applicant {applicant_id} not found")
                return success
        except sqlite3.Error as e:
            print(f" Database error: {e}")
            return False
    
    def get_statistics(self) -> Dict:
        """Get application statistics"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Total applications
            cursor.execute('SELECT COUNT(*) FROM applicants')
            total = cursor.fetchone()[0]
            
            # Status breakdown
            cursor.execute('SELECT status, COUNT(*) FROM applicants GROUP BY status')
            status_counts = dict(cursor.fetchall())
            
            return {
                'total': total,
                'status_breakdown': status_counts
            }

def save_application_record(full_name, email, phone, position, years_exp, skills, resume):
    db = JobApplicationDB()
    db.save_application(full_name, email, phone, position, years_exp, skills, resume)