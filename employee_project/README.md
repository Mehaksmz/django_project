# Employee Management System
A Django-based Employee Management System with RESTful APIs, database seeding, authentication, and analytics visualization.

---

## Project Overview
This project is a Employee Management System built with Django and Django REST Framework.
It allows you to manage employees, departments, attendance, and performance, with API endpoints for all operations and data visualizations using Chart.js.

---

## Features
- Employee, Department, Attendance, and Performance models.
- PostgreSQL database with environment-based configuration.
- Database seeding with fake data (Faker).
- RESTful CRUD APIs with filtering, pagination, and sorting.
- JWT authentication.
- Interactive API documentation (Swagger UI).
- Analytics visualizations (Chart.js).

---

## Tech Stack
- Backend: Django 4.x, Django REST Framework
- Database: PostgreSQL
- Authentication: Simple JWT
- API Docs: drf-yasg (Swagger)
- Environment: django-environ
- Fake Data: Faker
- Filtering: django-filter

## Folder Structure
employee_project/
├── employees/                # Employee app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── management/commands/seed_data.py
├── attendance/               # Attendance app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── employee_project/         # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
│   └── charts.html           # (Chart.js) visualizations
├── requirements.txt
├── .env.example
├── manage.py
└── README.md

## ⚙️ Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Mehaksmz/django_project.git
    cd django_project
    ```

2. **Create and Activate a Virtual Environment**

    ```bash
    conda create -n myvenv python=3.11
    conda activate myvenv
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**

    Copy `.env.example` to `.env` and fill in your settings:

    ```
    DEBUG=True
    SECRET_KEY=your-secret-key
    DATABASE_URL=postgres://user:password@localhost:5432/employee_db
    ```

5. **Apply Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Seed the Database with Fake Data**

    ```bash
    python manage.py seed_data
    ```

7. **Create a Superuser (for admin access)**

    ```bash
    python manage.py createsuperuser
    ```

8. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

---

## API Usage Guide

### Authentication

1. Obtain a token:

    ```http
    POST /api/token/
    {
      "username": "yourusername",
      "password": "yourpassword"
    }
    ```

2. Use the token in the Authorization header:

    ```
    Authorization: Bearer <your_token>
    ```

### API Endpoints

| Resource      | Endpoint                        | Methods                  |
|---------------|---------------------------------|--------------------------|
| Employees     | `/api/employees/`               | GET, POST                |
| Employee      | `/api/employees/{id}/`          | GET, PUT, PATCH, DELETE  |
| Departments   | `/api/departments/`             | GET, POST                |
| Department    | `/api/departments/{id}/`        | GET, PUT, PATCH, DELETE  |
| Attendance    | `/api/attendance/`              | GET, POST                |
| Attendance    | `/api/attendance/{id}/`         | GET, PUT, PATCH, DELETE  |
| Performance   | `/api/performance/`             | GET, POST                |
| Performance   | `/api/performance/{id}/`        | GET, PUT, PATCH, DELETE  |

#### Filtering & Pagination

- Filter employees by department:
    ```
    /api/employees/?department=<department_id>
    ```
- Filter by date joined:
    ```
    /api/employees/?date_joined=YYYY-MM-DD
    ```
- Pagination:
    ```
    /api/employees/?page=2
    ```

---

## Swagger API Docs

Visit [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) for interactive API documentation.

---

## Analytics & Visualization

Visit [http://127.0.0.1:8000/charts/](http://127.0.0.1:8000/charts/) to view employee analytics charts.

---