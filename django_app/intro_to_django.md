# Module 4.1 – Introduction to Django

> **Audience:** Java developers stepping into Python web development
> **Duration:** 1 hour

---

## 1. What is Django?

Django is a **high-level, batteries-included Python web framework** that encourages rapid development and clean, pragmatic design.

> **Java analogy:** Think of Django as **Spring Boot** for Python — it gives you ORM, routing, templates, auth, admin, and a dev server right out of the box.

### Key Philosophy

| Principle                            | Meaning                             |
| ------------------------------------ | ----------------------------------- |
| **DRY** – Don't Repeat Yourself      | Reuse code; avoid duplication       |
| **Convention over Configuration**    | Sensible defaults, minimal setup    |
| **Batteries Included**               | ORM, admin, auth, sessions built-in |
| **Explicit is better than implicit** | Clear, readable code (Python Zen)   |

### Real-world usage

- Instagram, Pinterest, Disqus, Mozilla — all built on Django
- Powers news sites, e-commerce, dashboards, REST APIs

---

## 2. MVC vs MVT Architecture

### MVC (Model-View-Controller) — what Java devs know

```
Request → Controller → Model (DB) → View (HTML) → Response
```

| Layer          | Role                                        |
| -------------- | ------------------------------------------- |
| **Model**      | Data / Business logic                       |
| **View**       | UI / HTML templates                         |
| **Controller** | Handles request, talks to Model, picks View |

> Example in Java Spring: `@Controller` class calls `@Service` → `@Repository` → returns a view name.

---

### MVT (Model-View-Template) — what Django uses

```
Request → URL Dispatcher → View → Model (ORM) → Template → Response
```

| Layer              | Django Equivalent  | Role                                         |
| ------------------ | ------------------ | -------------------------------------------- |
| **Model**          | `models.py`        | Defines DB schema + data logic               |
| **View**           | `views.py`         | Business logic, fetches data, picks template |
| **Template**       | `templates/*.html` | HTML + Django Template Language (DTL)        |
| **URL Dispatcher** | `urls.py`          | Routes URLs to the right View                |

#### Side-by-side comparison

```
MVC Controller  ←→  Django View  (handles request/response logic)
MVC View        ←→  Django Template  (the actual HTML rendered)
MVC Model       ←→  Django Model  (same idea — ORM-backed data)
```

> **Key difference:** In MVC the _View_ is what the user sees. In MVT the _Template_ is what the user sees, and the _View_ is closer to MVC's _Controller_.

#### MVT request-response flow (step by step)

```
Browser ──[GET /posts/]──►  urls.py
                              │
                              ▼
                          views.py  ──► models.py (ORM query)
                              │
                              ▼
                         template.html  (DTL renders data)
                              │
                              ▼
                         HTTP Response ──► Browser
```

---

## 3. Django vs Flask — When to Use Which

| Feature             | **Django**                              | **Flask**                             |
| ------------------- | --------------------------------------- | ------------------------------------- |
| **Type**            | Full-stack, batteries-included          | Micro-framework, minimalist           |
| **ORM**             | Built-in Django ORM                     | None (use SQLAlchemy separately)      |
| **Admin Panel**     | Auto-generated admin UI                 | None (build yourself)                 |
| **Auth**            | Built-in auth system                    | Flask-Login extension needed          |
| **Template Engine** | Django Template Language (DTL)          | Jinja2                                |
| **Forms**           | `forms.py` with validation              | WTForms extension                     |
| **Learning curve**  | Steeper (more conventions)              | Easier to start                       |
| **Flexibility**     | Less flexible (opinionated)             | Very flexible (unopinionated)         |
| **Best for**        | Large apps, CMS, e-commerce, dashboards | Small APIs, microservices, prototypes |

### When to choose Django ✅

- You need an **admin panel** quickly
- Building a **content-heavy site** (blog, news, CMS)
- Working in a **team** (Django enforces structure)
- You need **auth, sessions, forms** out of the box
- Database-driven applications

### When to choose Flask ✅

- Building a **REST API** or microservice
- **Learning** the basics of web frameworks first
- Small apps where Django would be overkill
- Need full **custom control** over every component

> **Java analogy:**
> Django = **Spring Boot** (full framework, auto-configuration)
> Flask = **Spark Java / Javalin** (lightweight, you wire everything)

---

## 4. Quick Setup Overview

```bash
# Step 1: Install Django (we use uv — modern Python package manager)
uv init myblog_project
cd myblog_project
uv add django

# Step 2: Create a Django project (generates project skeleton)
uv run django-admin startproject myblog .

# Step 3: Verify — start the development server
uv run python manage.py runserver
# Visit: http://127.0.0.1:8000
```

### Project structure after startproject

```
myblog/               ← Project package (config lives here)
│   settings.py       ← All settings (DB, apps, templates…)
│   urls.py           ← Root URL router
│   wsgi.py           ← Production WSGI entry point
│   asgi.py           ← Async entry point
manage.py             ← CLI tool (runserver, migrate, shell…)
```

### Key settings to know (`settings.py`)

```python
INSTALLED_APPS    # List of apps Django loads (your app goes here)
DATABASES         # DB config — default is SQLite (perfect for dev)
TEMPLATES         # Template engine config + directories
STATIC_URL        # URL prefix for CSS/JS/images
DEBUG             # True in dev, NEVER True in production
SECRET_KEY        # Cryptographic key — keep it secret!
```

### Useful `manage.py` commands

```bash
python manage.py runserver        # Start dev server
python manage.py startapp blog    # Create a new app
python manage.py makemigrations   # Generate migration files from models
python manage.py migrate          # Apply migrations to DB
python manage.py createsuperuser  # Create admin login
python manage.py shell            # Interactive Django shell
python manage.py dbshell          # Raw SQL shell
```

---

## Summary

- Django follows **MVT** — don't confuse Django's _View_ with MVC's _View_
- Django is the **Spring Boot of Python** — structured, full-featured, fast to build with
- Flask is lighter; Django is more complete — choose based on project size and team needs
- `manage.py` is your go-to CLI (like Maven goals but simpler)
- Everything starts with `django-admin startproject` and grows from there
