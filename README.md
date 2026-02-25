# Django Authentication & Profile Management System

A Django-based web application implementing secure user registration,
authentication, and profile management using Django’s built-in authentication framework.

## Features

- User registration with validation
- Secure login and logout
- Custom Profile model (One-to-One with User)
- Profile creation and update
- Image upload handling
- Session-based authentication
- Dynamic navigation rendering
- Template inheritance structure

## Tech Stack

- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite

---

## How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/IfreenIsrar/django-auth-profile-system.git
cd django-auth-profile-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the server

```bash
python manage.py runserver
```

### 7. Open in browser

http://127.0.0.1:8000/

### Watch project walkthrough here:
[LinkedIn Demo Video](https://www.linkedin.com/feed/update/urn:li:activity:7427412016912420865/)
