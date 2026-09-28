# InternTrack – Internship Application Management System

InternTrack is a web-based internship application management system developed to help students organize and manage their internship applications in one place.

The application allows users to add, view, edit, search, and delete internship applications while tracking important details such as company, role, location, application date, deadline, status, interview date, stipend, application link, and notes.

---

## 🎯 Objective

The main objective of InternTrack is to provide students with a simple and organized platform for managing internship applications.

The project demonstrates:

- Dynamic web application development
- Server-side data processing
- Database integration
- Git version control
- Automated testing
- Continuous Integration using GitHub Actions
- Continuous Deployment using Render

---

## 🚀 Features

### 1. Internship Dashboard

The dashboard displays all internship applications along with summary statistics:

- Total applications
- Applied
- Interview
- Selected
- Rejected

### 2. Add Internship

Users can add a new internship application with:

- Company Name
- Job Role
- Location
- Application Date
- Application Deadline
- Status
- Interview Date
- Stipend
- Application Link
- Notes

### 3. Edit Internship

Existing internship applications can be updated whenever application details change.

### 4. Delete Internship

Users can remove an internship application from the system.

### 5. Search Internship

The dashboard provides a search feature to quickly find internships by company or role.

### 6. Application Status

Internship applications can have different statuses:

- Applied
- Shortlisted
- Interview
- Selected
- Rejected

### 7. Database Storage

Internship application data is stored using SQLite.

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python 3 |
| Web Framework | Flask |
| Database | SQLite |
| Frontend | HTML5, CSS3, JavaScript |
| Template Engine | Jinja2 |
| Testing | pytest |
| CI/CD | GitHub Actions |
| Application Server | Gunicorn |
| Deployment | Render |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```text
InternTrack/
│
├── app.py
├── requirements.txt
├── Procfile
├── README.md
├── .gitignore
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   └── edit.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── tests/
│   └── test_app.py
│
└── .github/
    └── workflows/
        └── ci.yml
