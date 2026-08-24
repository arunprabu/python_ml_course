"""
Step 24: Custom management command — seed_data
         Run with:  uv run python manage.py seed_data

         This creates sample categories, a superuser, and sample posts
         so the demo works immediately after setup.

         Like a Spring Boot DataLoader / CommandLineRunner.
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Category, Post


class Command(BaseCommand):
    help = "Seed the database with sample categories and posts for the demo"

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("Seeding demo data..."))

        # ----------------------------------------------------------------
        # 1. Create superuser  (password: admin123)
        # ----------------------------------------------------------------
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123',
                first_name='Admin',
                last_name='User',
            )
            self.stdout.write(self.style.SUCCESS("  Created superuser: admin / admin123"))
        else:
            admin = User.objects.get(username='admin')
            self.stdout.write("  Superuser 'admin' already exists — skipping.")

        # ----------------------------------------------------------------
        # 2. Create categories
        # ----------------------------------------------------------------
        categories_data = [
            {'name': 'Django',    'slug': 'django'},
            {'name': 'Python',    'slug': 'python'},
            {'name': 'Machine Learning', 'slug': 'machine-learning'},
            {'name': 'Web Development', 'slug': 'web-development'},
        ]

        for cat_data in categories_data:
            cat, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={'name': cat_data['name']},
            )
            if created:
                self.stdout.write(f"  Created category: {cat.name}")

        django_cat = Category.objects.get(slug='django')
        python_cat = Category.objects.get(slug='python')
        ml_cat     = Category.objects.get(slug='machine-learning')

        # ----------------------------------------------------------------
        # 3. Create sample posts
        # ----------------------------------------------------------------
        posts_data = [
            {
                'title': 'Getting Started with Django',
                'slug': 'getting-started-with-django',
                'category': django_cat,
                'content': (
                    "Django is a high-level Python web framework that encourages rapid development.\n\n"
                    "It follows the MVT (Model-View-Template) architecture pattern.\n\n"
                    "Key features:\n"
                    "- Built-in ORM for database operations\n"
                    "- Automatic admin interface\n"
                    "- Robust URL routing system\n"
                    "- Template engine (DTL)\n"
                    "- Built-in authentication system\n\n"
                    "Getting started is as simple as:\n"
                    "  pip install django\n"
                    "  django-admin startproject mysite\n"
                    "  python manage.py runserver"
                ),
                'published': True,
            },
            {
                'title': 'Django ORM: CRUD Operations Explained',
                'slug': 'django-orm-crud-operations',
                'category': django_cat,
                'content': (
                    "The Django ORM lets you interact with your database using Python objects.\n\n"
                    "CREATE:\n"
                    "  Post.objects.create(title='Hello', ...)\n\n"
                    "READ:\n"
                    "  Post.objects.all()           # all records\n"
                    "  Post.objects.filter(...)     # filtered records\n"
                    "  Post.objects.get(id=1)       # single record\n\n"
                    "UPDATE:\n"
                    "  post = Post.objects.get(id=1)\n"
                    "  post.title = 'Updated'\n"
                    "  post.save()\n\n"
                    "DELETE:\n"
                    "  Post.objects.get(id=1).delete()\n\n"
                    "No SQL needed — the ORM generates it for you!"
                ),
                'published': True,
            },
            {
                'title': 'Python List Comprehensions',
                'slug': 'python-list-comprehensions',
                'category': python_cat,
                'content': (
                    "List comprehensions are a concise way to create lists in Python.\n\n"
                    "Basic syntax:\n"
                    "  [expression for item in iterable if condition]\n\n"
                    "Examples:\n"
                    "  squares = [x**2 for x in range(10)]\n"
                    "  evens   = [x for x in range(20) if x % 2 == 0]\n\n"
                    "Java equivalent (Stream API):\n"
                    "  List<Integer> squares = IntStream.range(0, 10)\n"
                    "      .map(x -> x * x)\n"
                    "      .boxed().collect(Collectors.toList());\n\n"
                    "Python's version is much shorter and readable!"
                ),
                'published': True,
            },
            {
                'title': 'Introduction to Machine Learning with Python',
                'slug': 'intro-to-machine-learning',
                'category': ml_cat,
                'content': (
                    "Machine Learning (ML) enables computers to learn from data without being explicitly programmed.\n\n"
                    "Core concepts:\n"
                    "- Supervised Learning: learn from labeled data (classification, regression)\n"
                    "- Unsupervised Learning: find patterns in unlabeled data (clustering)\n"
                    "- Reinforcement Learning: learn by reward and punishment\n\n"
                    "Popular Python libraries:\n"
                    "- scikit-learn: classical ML algorithms\n"
                    "- pandas: data manipulation\n"
                    "- numpy: numerical computation\n"
                    "- matplotlib: data visualization\n\n"
                    "A simple workflow:\n"
                    "  1. Load data (pandas)\n"
                    "  2. Pre-process / clean\n"
                    "  3. Split into train/test\n"
                    "  4. Choose a model\n"
                    "  5. Train: model.fit(X_train, y_train)\n"
                    "  6. Evaluate: model.score(X_test, y_test)"
                ),
                'published': True,
            },
            {
                'title': 'Django Views and URL Routing Deep Dive',
                'slug': 'django-views-url-routing',
                'category': django_cat,
                'content': (
                    "URL routing in Django maps incoming HTTP requests to Python functions (views).\n\n"
                    "urls.py:\n"
                    "  urlpatterns = [\n"
                    "      path('', views.home, name='home'),\n"
                    "      path('posts/<slug:slug>/', views.detail, name='detail'),\n"
                    "  ]\n\n"
                    "A simple view:\n"
                    "  def home(request):\n"
                    "      posts = Post.objects.all()\n"
                    "      return render(request, 'home.html', {'posts': posts})\n\n"
                    "Named URLs allow us to generate links in templates:\n"
                    "  {% url 'detail' post.slug %}  →  /posts/my-slug/"
                ),
                'published': True,
            },
        ]

        for post_data in posts_data:
            post, created = Post.objects.get_or_create(
                slug=post_data['slug'],
                defaults={
                    'title':     post_data['title'],
                    'category':  post_data['category'],
                    'author':    admin,
                    'content':   post_data['content'],
                    'published': post_data['published'],
                },
            )
            if created:
                self.stdout.write(f"  Created post: {post.title}")

        self.stdout.write(self.style.SUCCESS("\nDone! Demo data seeded successfully."))
        self.stdout.write("")
        self.stdout.write("  Admin panel:  http://127.0.0.1:8000/admin/")
        self.stdout.write("  Login:        admin / admin123")
        self.stdout.write("  Blog home:    http://127.0.0.1:8000/")
