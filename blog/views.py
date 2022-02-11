from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index(request):
  post = Post.objects.all()
  return render(request, "blog/index.html", {"posts": post})

def post_detail(request, slug):
  post = get_object_or_404(Post, slug=slug)
  return render(request, "blog/post_detail.html", {"post": post})