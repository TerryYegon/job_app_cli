import sqlite3
from typing import List

class Application:
    def __init__(self, id, job_id, applicant_name, email):
        self.id = id
        self.job_id = job_id
        self.applicant_name = applicant_name
        self.email = email

    @staticmethod
    def create(job_id, applicant_name, email):
        conn = sqlite3.connect('job_applications.db')
        c = conn.cursor()
        c.execute('INSERT INTO applications (job_id, applicant_name, email) VALUES (?, ?, ?)', (job_id, applicant_name, email))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(app_id):
        conn = sqlite3.connect('job_applications.db')
        c = conn.cursor()
        c.execute('DELETE FROM applications WHERE id = ?', (app_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all() -> List['Application']:
        conn = sqlite3.connect('job_applications.db')
        c = conn.cursor()
        c.execute('SELECT id, job_id, applicant_name, email FROM applications')
        apps = [Application(*row) for row in c.fetchall()]
        conn.close()
        return apps

    @staticmethod
    def find_by_id(app_id):
        conn = sqlite3.connect('job_applications.db')
        c = conn.cursor()
        c.execute('SELECT id, job_id, applicant_name, email FROM applications WHERE id = ?', (app_id,))
        row = c.fetchone()
        conn.close()
        return Application(*row) if row else None

    @staticmethod
    def get_by_job(job_id) -> List['Application']:
        conn = sqlite3.connect('job_applications.db')
        c = conn.cursor()
        c.execute('SELECT id, job_id, applicant_name, email FROM applications WHERE job_id = ?', (job_id,))
        apps = [Application(*row) for row in c.fetchall()]
        conn.close()
        return apps
