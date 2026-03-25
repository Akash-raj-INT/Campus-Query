# CampusQuery – Unified Campus Knowledge Platform

CampusQuery is a Django-based web application designed for college students to share notes, ask questions, and collaborate in an organized way. It replaces unstructured WhatsApp groups with a centralized, searchable platform.

---

## 🚀 Features

* 📂 Notes Upload & Download (Subject & Semester wise)
* ❓ Q&A Forum with threaded answers
* 🎯 Mentor Matching (Senior–Junior connection)
* 🔍 Smart Search with filters
* ⭐ Rating & Feedback System
* 🔐 Secure Authentication (College Email आधारित)

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Database:** PostgreSQL
* **API:** Django REST Framework
* **Frontend:** HTML, CSS, Bootstrap
* **Authentication:** JWT / Django Auth

---

## 📁 Project Structure

```
CampusQuery/
│── manage.py
│── requirements.txt
│── README.md
│
├── campusquery/        # Main project settings
├── users/              # Authentication & profiles
├── notes/              # Notes management module
├── qa_forum/           # Q&A system
│
├── templates/          # HTML templates
├── static/             # CSS, JS, images
```

---

## ⚙️ Installation & Setup

1. Clone the repository

```
git clone https://github.com/your-username/CampusQuery.git
cd CampusQuery
```

2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Apply migrations

```
python manage.py migrate
```

5. Run the server

```
python manage.py runserver
```

---

## 📊 Current Status

* ✅ User Authentication
* ✅ Notes Management
* ✅ Q&A Forum
* 🚧 Study Groups (In Progress)

---

## 🔮 Future Enhancements

* Celery for background tasks
* Elasticsearch for advanced search
* Mobile API support
* Admin analytics dashboard

---

## 🤝 Contribution

Contributions are welcome!
Feel free to fork the repo and submit pull requests.

---

## 📌 Author

**Akash Raj**
Computer Science Student | Full Stack Developer | Data Scientist

---

## 🛠️ Deployment Notes (Added)

- Procfile now uses `web: gunicorn campusquery.campusquery.wsgi`.
- `runtime.txt` set to `python-3.11.9` for compatibility with deployment platforms.
- Simplified `requirements.txt` to avoid dependency conflicts in Render/Vercel.

---


