from django.urls import path
from . import views

# Step 14: URL patterns — map URLs to view functions
app_name = 'blog'

urlpatterns = [
    # /  →  list all posts
    path('', views.post_list, name='post_list'),
    # /posts/my-slug/  →  single post
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
]
