from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Category, Post

# Create your views here.
def index(request):
    #posts = Post.objects.all()
    posts = Post.objects.filter(id__gte=2)
    context={"posts":posts}
    return render(request,'posts/posts.html',context)

def getPost(request,post_id):
    post = Post.objects.get(id=post_id)
    context = {"post":post}
    return render(request,'posts/post.html',context=context)

def getCategories(request):
    categories = Category.objects.all()
    context = {"categories" : categories}
    return render(request,'categories/categories.html',context = context)

def getCategory(request,category_id):
    #category = Category.objects.get(pk=category_id)
    category = get_object_or_404(Category,pk=category_id)
    context = {"category":category}
    return render(request,'posts/category.html',context=context)