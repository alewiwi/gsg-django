from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
#from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic import View,TemplateView


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

class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "post_list"

# class PostListView(ListView):
#     model = Post
#     context_object_name = "post_list"
#     template_name = "posts/post_list.html"
    
#     # def get_queryset(self):
#     #     return Post.objects.order_by("-title")[:10]
    
    
class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post_details'
    template_name = 'posts/post_details.html'
# class PostDetailView(DetailView):
#     context_object_name = 'post_details'
#     template_name = 'posts/post_details.html'
    
#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Post,id=id_)

class SimpleView(TemplateView):
    template_name= 'posts/simple_view.html'