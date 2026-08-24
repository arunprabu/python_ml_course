# Django Blog – Day 4 Hands-on Demo

A minimal blog app built with Django 6 + uv. Covers Models, ORM, Admin, Views, URL routing, and Templates.

---

## Steps to build from scratch

### Step 1 – Init the project with uv

```bash
uv init my_blog_demo
cd my_blog_demo
uv add django
```

---

### Step 2 – Create the Django project skeleton

```bash
uv run django-admin startproject myblog .
```

This generates:

```
manage.py        ← CLI tool
myblog/
  settings.py    ← configuration
  urls.py        ← root URL router
```

---

### Step 3 – Create the blog app

```bash
uv run python manage.py startapp blog
```

---

### Step 4 – Register the app in settings.py

Open `myblog/settings.py` and add `'blog'` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'blog',
]
```

---

### Step 5 – Define models (blog/models.py)

```python
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title      = models.CharField(max_length=200)
    slug       = models.SlugField(max_length=200, unique=True)
    category   = models.ForeignKey(Category, on_delete=models.CASCADE)
    author     = models.ForeignKey(User, on_delete=models.CASCADE)
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published  = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

---

### Step 6 – Run migrations

```bash
uv run python manage.py makemigrations   # generate SQL from models
uv run python manage.py migrate          # apply to DB (creates tables)
```

**Which database is this writing to?** SQLite — Django's default. See `myblog/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

No server process, no connection string, no env vars. `migrate` just creates the file `db.sqlite3` in the project root.

#### Why isn't SQLite listed in `pyproject.toml`?

Because it isn't a third-party package — it ships with Python itself. CPython's standard library includes the `sqlite3` module (a C extension linked against a SQLite library bundled at build time), and Django's `django.db.backends.sqlite3` backend simply does `import sqlite3`. Nothing to install, nothing to declare.

Prove it in one line:

```bash
uv run python -c "import sqlite3; print(sqlite3.sqlite_version)"
```

Every other backend _does_ need a driver added to `dependencies`:

| Database      | Driver package     | Add to pyproject? |
| ------------- | ------------------ | ----------------- |
| SQLite        | `sqlite3` (stdlib) | not needed        |
| PostgreSQL    | `psycopg[binary]`  | required          |
| MySQL/MariaDB | `mysqlclient`      | required          |
| Oracle        | `oracledb`         | required          |

That's exactly why `startproject` defaults to SQLite: a brand-new project runs with zero database setup. The tradeoff is that it's a single file with limited concurrent writes, so real deployments swap in PostgreSQL — change `ENGINE` to `django.db.backends.postgresql`, add the host/user/password keys, and _then_ run `uv add "psycopg[binary]"`.

---

### Step 7 – Register models in admin (blog/admin.py)

```python
from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Category, Post

# Hide built-in auth models from admin — not needed for this demo
admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display  = ['title', 'category', 'author', 'published']
    list_editable = ['published']
```

---

### Step 8 – Create a superuser

```bash
uv run python manage.py createsuperuser
```

Or use the seed command (included in this project):

```bash
uv run python manage.py seed_data   # creates admin/admin123 + sample posts
```

---

### Step 9 – Write views (blog/views.py)

```python
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/post_list.html', {'posts': posts, 'page_title': 'All Posts'})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/post_detail.html', {'post': post, 'page_title': post.title})
```

---

### Step 10 – Wire up URLs

**blog/urls.py** (new file):

```python
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
]
```

**myblog/urls.py** – include blog URLs:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

---

### Step 11 – Create templates

**Directory:** `blog/templates/blog/`

**base.html** – parent template (navbar + layout):

```html
{% load static %}
<!DOCTYPE html>
<html>
  <head>
    <title>{% block title %}MyBlog{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}" />
  </head>
  <body>
    <nav class="navbar">
      <a href="{% url 'blog:post_list' %}">MyBlog</a>
    </nav>
    <div class="container">
      <main>{% block content %}{% endblock %}</main>
    </div>
  </body>
</html>
```

**post_list.html** – list all posts:

```html
{% extends "blog/base.html" %} {% block content %} {% for post in posts %}
<div class="card">
  <h2><a href="{% url 'blog:post_detail' post.slug %}">{{ post.title }}</a></h2>
  <p>{{ post.created_at|date:"M d, Y" }} | {{ post.category.name }}</p>
  <p>{{ post.content|truncatewords:30 }}</p>
</div>
{% empty %}
<p>No posts yet.</p>
{% endfor %} {% endblock %}
```

**post_detail.html** – single post:

```html
{% extends "blog/base.html" %} {% block content %}
<a href="{% url 'blog:post_list' %}">&larr; Back</a>
<h1>{{ post.title }}</h1>
<p>{{ post.created_at|date:"F d, Y" }} | {{ post.category.name }}</p>
<div>{{ post.content|linebreaks }}</div>
{% endblock %}
```

---

### Step 12 – Add static files

Create `static/css/style.css` and add `STATICFILES_DIRS` in settings:

```python
STATICFILES_DIRS = [BASE_DIR / 'static']
```

---

### Step 13 – Run the server

```bash
uv run python manage.py runserver
```

| URL                                   | Page                  |
| ------------------------------------- | --------------------- |
| http://127.0.0.1:8000/                | Blog home (all posts) |
| http://127.0.0.1:8000/posts/\<slug\>/ | Single post           |
| http://127.0.0.1:8000/admin/          | Admin panel           |

Admin login: `admin` / `admin123` (after running `seed_data`)

---

## Key Django concepts covered

| Concept              | File              | What it does                    |
| -------------------- | ----------------- | ------------------------------- |
| Models               | `blog/models.py`  | Define DB schema                |
| Migrations           | `0001_initial.py` | Auto-generated SQL              |
| ORM                  | `views.py`        | `Post.objects.filter(...)`      |
| Admin                | `blog/admin.py`   | Auto-generated CRUD UI          |
| Views (FBV)          | `blog/views.py`   | Handle request, return response |
| URL routing          | `blog/urls.py`    | Map URLs to views               |
| Templates            | `templates/blog/` | HTML with DTL                   |
| Template inheritance | `base.html`       | `extends` + `block`             |
| Static files         | `static/css/`     | CSS, JS, images                 |

---

## Optional – Switching from SQLite to PostgreSQL

Not required for this demo. This is what the change looks like in a real deployment, where SQLite's single-file / single-writer model stops being enough.

### 1. Add the driver

Unlike SQLite, PostgreSQL needs a third-party driver — this is the dependency that _does_ belong in `pyproject.toml`:

```bash
uv add "psycopg[binary]"
```

The `[binary]` extra pulls a pre-compiled wheel, so you don't need Postgres dev headers or a C compiler locally. (In production, `psycopg[c]` or plain `psycopg` built against the system libpq is the usual choice.)

### 2. Run a PostgreSQL server

Docker is the quickest for a workshop — no system-wide install:

```bash
docker run --name myblog-pg \
  -e POSTGRES_DB=myblog \
  -e POSTGRES_USER=myblog \
  -e POSTGRES_PASSWORD=myblog123 \
  -p 5432:5432 \
  -d postgres:17
```

Or with a locally installed Postgres (`brew install postgresql@17`):

```bash
createdb myblog
createuser myblog --pwprompt
psql -c "GRANT ALL PRIVILEGES ON DATABASE myblog TO myblog;"
```

### 3. Point Django at it (`myblog/settings.py`)

Replace the `DATABASES` block:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myblog',
        'USER': 'myblog',
        'PASSWORD': 'myblog123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

Note what changed vs. SQLite: `NAME` is now a database name on a server, not a file path, and four new keys appear because there's a network connection and an auth handshake involved.

Don't hard-code credentials in real projects — read them from the environment:

```python
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ.get('POSTGRES_HOST', '127.0.0.1'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
        'CONN_MAX_AGE': 60,   # reuse connections instead of reconnecting per request
    }
}
```

### 4. Create the schema and verify

The new database is empty — migrations must run again against it:

```bash
uv run python manage.py migrate
uv run python manage.py seed_data      # re-create admin/admin123 + sample posts
uv run python manage.py runserver
```

Confirm Django is actually talking to Postgres:

```bash
uv run python manage.py dbshell         # should drop you into psql
```

### 5. Moving existing data across (if you need it)

Switching `ENGINE` does **not** copy your rows — `db.sqlite3` is left untouched on disk and simply stops being read. To carry the demo data over, dump it _before_ editing settings and load it after:

```bash
# with settings still on SQLite
uv run python manage.py dumpdata --natural-foreign --natural-primary \
  -e contenttypes -e auth.Permission > data.json

# switch DATABASES to postgresql, then:
uv run python manage.py migrate
uv run python manage.py loaddata data.json
```

Excluding `contenttypes` and `auth.Permission` avoids primary-key collisions with the rows `migrate` already created in the fresh database.

### Gotchas worth knowing

| Gotcha                 | SQLite                             | PostgreSQL                                           |
| ---------------------- | ---------------------------------- | ---------------------------------------------------- |
| Server                 | none — a file                      | must be running before Django starts                 |
| Concurrent writes      | one writer at a time               | full MVCC, many writers                              |
| Schema changes         | table rebuilds, very permissive    | strict — a bad migration can fail on real data       |
| String comparison      | case-insensitive `LIKE` by default | case-sensitive; use `__iexact` / `__icontains`       |
| Missing driver symptom | n/a                                | `ImproperlyConfigured: Error loading psycopg module` |
