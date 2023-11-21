from django.shortcuts import render
from .models import Post

def main(request):
    posts = Post.objects.all()
    for post in posts:
        print(post.image)
    return render(request=request,template_name='index.html',context={'posts':posts})

def detail(request,pk):
    post = Post.objects.get(id=pk)
    return 

 
