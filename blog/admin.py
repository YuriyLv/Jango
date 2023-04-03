from django.contrib import admin
from .models import Post
from .models import Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('index', 'title', 'author', 'data')

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display_2 = ('category_name')