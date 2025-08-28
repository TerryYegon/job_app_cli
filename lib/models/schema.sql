-- SQL schema for jobs and applications tables
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id INTEGER NOT NULL,
    applicant_name TEXT NOT NULL,
    email TEXT NOT NULL,
    FOREIGN KEY(job_id) REFERENCES jobs(id)
);
