# CampusQuery

CampusQuery is a Django web app for sharing notes, asking questions, and helping students collaborate in one searchable place.

## Stack

- Python 3.11
- Django 5.2
- Django REST Framework
- PostgreSQL on Render
- WhiteNoise for static files

## Project Layout

The Django project is nested inside the repository:

```text
CampusQuery/
|-- requirements.txt
|-- Procfile
|-- render.yaml
`-- campusquery/
    |-- manage.py
    |-- db.sqlite3
    |-- core/
    `-- campusquery/
        |-- settings.py
        |-- urls.py
        `-- wsgi.py
```

## Local Setup

1. Create and activate a virtual environment.

```powershell
python -m venv venv
.\venv\Scripts\activate
```

2. Install dependencies.

```powershell
pip install -r requirements.txt
```

3. Create your local environment variables from [`.env.example`](/c:/Users/ASUS/Desktop/Python%20Full%20Stack/CampusQuery/.env.example).

```text
SECRET_KEY=replace-me-with-a-long-random-secret
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

4. Move into the Django app directory.

```powershell
cd campusquery
```

5. Run migrations.

```powershell
python manage.py migrate
```

6. Start the development server.

```powershell
python manage.py runserver
```

## Render Deployment

This repo includes both [`Procfile`](/c:/Users/ASUS/Desktop/Python%20Full%20Stack/CampusQuery/Procfile) and [`render.yaml`](/c:/Users/ASUS/Desktop/Python%20Full%20Stack/CampusQuery/render.yaml) with the correct nested-directory commands.

Build command:

```text
cd campusquery && pip install -r ../requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

Start command:

```text
cd campusquery && gunicorn campusquery.wsgi --bind 0.0.0.0:$PORT
```

Set these Render environment variables:

- `SECRET_KEY`
- `DEBUG=False`
- `ALLOWED_HOSTS=your-service.onrender.com`
- `DATABASE_URL`

## Notes

- `requirements.txt` is pinned for Python 3.11 compatibility on Render.
- Render now requires `SECRET_KEY` to be set explicitly in the environment.
- If your local virtualenv still has Django 6 installed, recreate it so local behavior matches deployment.
