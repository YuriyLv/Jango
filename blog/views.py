from django.shortcuts import render
from django.views.generic.base import View
from .models import Post
from .models import Category

class PostView(View):
    '''view post'''
    def get(self, request):
        posts = Post.objects.all()
        categorys = Category.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts, 'category_list': categorys})

class PostCatView(View):
    def get(self, request, cat):
        category = Category.objects.get(category_name=cat)
        posts = Post.objects.filter(index_id=category.id)
        categorys = Category.objects.all()
        return render(request, 'blog/blog_detail.html', {'post_list': posts, 'category_list': categorys})


