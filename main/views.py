from django.shortcuts import render, get_object_or_404
from .models import Blog, Contact
from django.utils import timezone

# Create your views here.
def index(request):
    articles = Blog.objects.all()
    return render(request, 'main/index.html', {'articles': articles})

def blog(request):
    articles = Blog.objects.all()
    return render(request, 'main/blog.html', {"articles": articles})

def article_details(request, blog_id):
    article = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'main/article_details.html', {"article": article})

def covid_stats(request):
    return render(request, 'main/covid_stats.html')

def success(request):
    return render(request, 'main/success.html')

def contact(request):
    if request.method == 'POST':
        if request.POST['sender_name'] and request.POST['sender_mail'] and request.POST['sender_subject'] and request.POST['sender_message']:
            contact = Contact()
            contact.sender_name = request.POST['sender_name']
            contact.sender_mail = request.POST['sender_mail']
            contact.sender_subject = request.POST['sender_subject']
            contact.sender_message = request.POST['sender_message']
            contact.sent_at = timezone.now()
            contact.save()
            return render(request, 'main/success.html')
    return render(request, 'main/contact.html')
