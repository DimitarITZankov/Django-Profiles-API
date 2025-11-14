# Django Profiles API

A RESTful API built with Django and Django REST Framework to manage user profiles.
Supports a custom user model, secure password handling, and full CRUD operations for user data.
Django-REST-API

🚀 Features

Custom user model (UserProfile)

Secure password handling with set_password()

CRUD operations for user profiles

Django Admin integration

REST Framework browsable API

Clean structure: models, serializers, views, and managers separated

🧩 Tech Stack

Python

Django

Django REST Framework

SQLite (dev database)

Optional Vagrant environment

🔧 Installation
git clone https://github.com/DimitarITZankov/Django-Profiles-API.git
cd Django-Profiles-API

Create virtual environment:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Create superuser:
python manage.py createsuperuser

Run the server:
python manage.py runserver
API is available at:
http://127.0.0.1:8000/


🗂️ Project Structure
/api_profiles
    ├── serializers.py
    ├── models.py
    ├── views.py
    ├── urls.py
/ProfilesApiProject
    ├── settings.py
    ├── urls.py
manage.py
requirements.txt


📡 API Endpoints
GET /api/register/ – list profiles
POST /api/register/ – create profile
GET /api/register/<id>/ – retrieve profile
PUT /api/register/<id>/ – update profile
PATCH /api/register/<id>/ – partial update
DELETE /api/register/<id>/ – delete profile
