from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def blog(request):
    articles = Blog.objects.all()
    return render(request, 'main/blog.html', {"articles": articles})

def blog_details(request):
    pass