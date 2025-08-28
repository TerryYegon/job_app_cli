# Job Application CLI

A command-line application to manage jobs and applications, demonstrating OOP, ORM, and CLI best practices.

## Features
- Create, list, and delete jobs
- Create, list, and delete applications
- View all applications for a specific job
- Input validation and error handling

## Directory Structure
```
lib/
  cli.py           # Main CLI interface
  helpers.py       # Helper functions
  debug.py         # Debug helpers
  models/
    __init__.py
    job.py         # Job model (one)
    application.py # Application model (many)
```

## Usage
1. Ensure you have Python 3 and `pipenv` installed.
2. Install dependencies:
   ```bash
   pipenv install
   pipenv shell
   ```
3. Run the CLI:
   ```bash
   python lib/cli.py
   ```

## Models
- **Job**: Represents a job posting. Has many applications.
- **Application**: Represents an application to a job. Belongs to a job.

## ORM Methods
Each model supports:
- `create`
- `delete`
- `get_all`
- `find_by_id`

## CLI Commands
- Create, list, delete jobs
- Create, list, delete applications
- View applications for a job

## License
MIT
