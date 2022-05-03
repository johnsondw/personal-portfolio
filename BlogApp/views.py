from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def blog(request):
    # posts = Post.objects.all()
    posts = Post.objects.order_by('-datePosted')
    return render(request, 'BlogApp/blog.html', {'posts':posts})

def post(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    return render(request, 'BlogApp/post.html', {'post':post})
