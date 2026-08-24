from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Category, Post

# Hide built-in auth models — not needed for this demo
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

