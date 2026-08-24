from django.shortcuts import render, get_object_or_404
from .models import Post


# Step 13a: List all published posts
# GET /  →  runs this function  →  returns rendered HTML
def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'page_title': 'All Posts',
    })


# Step 13b: Show one post by its slug
# GET /posts/<slug>/
def post_detail(request, slug):
    # Returns 404 automatically if not found
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'page_title': post.title,
    })

