# Student Management System

A Student Management System REST API built using Django and Django REST Framework.

## Technologies

- Python
- Django
- Django REST Framework
- SQLite
- Postman

## Features

- Student CRUD operations
- Course CRUD operations
- Enrollment CRUD operations
- REST API endpoints
- Data validation
- Student-Course relationship management

## API Testing

The REST APIs are tested using Postman.

### Students

| Method | Endpoint |
|---|---|
| GET | `/api/students/` |
| POST | `/api/students/` |
| GET | `/api/students/{id}/` |
| PUT | `/api/students/{id}/` |
| PATCH | `/api/students/{id}/` |
| DELETE | `/api/students/{id}/` |

### Courses

| Method | Endpoint |
|---|---|
| GET | `/api/courses/` |
| POST | `/api/courses/` |
| GET | `/api/courses/{id}/` |
| PUT | `/api/courses/{id}/` |
| PATCH | `/api/courses/{id}/` |
| DELETE | `/api/courses/{id}/` |

### Enrollments

| Method | Endpoint |
|---|---|
| GET | `/api/enrollments/` |
| POST | `/api/enrollments/` |
| GET | `/api/enrollments/{id}/` |
| PUT | `/api/enrollments/{id}/` |
| PATCH | `/api/enrollments/{id}/` |
| DELETE | `/api/enrollments/{id}/` |

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Ranjityadav101/student-management-system_API
cd cd student-management-system-api
