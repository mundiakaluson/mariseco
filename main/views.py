from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def blog(request):
    articles = Blog.objects.all()
    return render(request, 'main/blog.html', {"articles": articles})

def article_details(request, blog_id):
    article = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'main/article_details.html', {"article": article})
