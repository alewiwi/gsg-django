from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context={"posts":posts}
    return render(request,'posts/posts.html',context)

def getPost(request,post_id):
    post = Post.objects.get(id=post_id)
    context = {"post":post}
    return render(request,'posts/post.html',context=context)

