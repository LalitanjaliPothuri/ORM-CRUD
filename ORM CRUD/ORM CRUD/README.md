# CRUD_ORM_PROJECT

## Project Overview

A professional Full-Stack Student Management System built with Python Flask, SQLAlchemy ORM, SQLite, HTML5, CSS3, and vanilla JavaScript. The application supports Create, Read, Update, and Delete operations for student records while storing data permanently in a SQLite database.

## Features

- Add new student records with name and age
- Display all students in a responsive data table
- Edit student records inline using the same form
- Delete student records with a confirmation prompt
- Server-side validation for required fields and age range
- Flash messages for user feedback
- Modern responsive UI with a clean card layout
- Automatic SQLite database creation using SQLAlchemy ORM

## Installation

1. Open a terminal in the project folder.
2. Create a virtual environment (recommended):

```bash
python -m venv venv
```

3. Activate the virtual environment:

- Windows:
  ```bash
  venv\Scripts\activate
  ```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## Project Structure

```
CRUD_ORM_PROJECT/
│
├── app.py
├── db.py
├── models.py
├── requirements.txt
├── students.db
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

## ORM Explanation

This project uses SQLAlchemy ORM for database management. The `Student` class in `models.py` maps to the `students` table in SQLite. SQLAlchemy handles SQL generation and data persistence, so the app interacts with Python objects instead of raw SQL queries.

## Notes

- The database file `students.db` is created automatically when the app runs.
- Update the `SECRET_KEY` in `app.py` for production.
- No raw SQL queries are used; all database operations are performed via SQLAlchemy ORM.
