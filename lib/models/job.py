import sqlite3
from typing import List

class Job:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        self._title = value

    @staticmethod
    def create(title, description):
        conn = sqlite3.connect('job_applications.db')
        c = conn.cursor()
        c.execute('INSERT INTO jobs (title, description) VALUES (?, ?)', (title, description))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(job_id):
        conn = sqlite3.connect('job_applications.db')
        c = conn.cursor()
        c.execute('DELETE FROM jobs WHERE id = ?', (job_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all() -> List['Job']:
        conn = sqlite3.connect('job_applications.db')
        c = conn.cursor()
        c.execute('SELECT id, title, description FROM jobs')
        jobs = [Job(*row) for row in c.fetchall()]
        conn.close()
        return jobs

    @staticmethod
    def find_by_id(job_id):
        conn = sqlite3.connect('job_applications.db')
        c = conn.cursor()
        c.execute('SELECT id, title, description FROM jobs WHERE id = ?', (job_id,))
        row = c.fetchone()
        conn.close()
        return Job(*row) if row else None
