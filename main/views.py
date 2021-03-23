from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Contact, WebContent, Comment, Profile
from django.utils import timezone
from .forms import CommentForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    web_content = get_object_or_404(WebContent)
    return render(request, 'main/index.html', {"web_content": web_content})

def blog(request):
    articles = Blog.objects.all()
    return render(request, 'main/blog.html', {"articles": articles})

def article_details(request, blog_id):
    article = get_object_or_404(Blog, pk=blog_id)
    user_comments = Comment.objects.all()
    comment_count = Comment.objects.all().count()
    if request.method == 'POST':
        if request.POST['user_name'] and request.POST['user_email'] and request.POST['user_comment']:
            comments = Comment()
            comments.name = request.POST['user_name']
            comments.post = article
            comments.created_on = timezone.now()
            comments.email = request.POST['user_email']
            comments.comment = request.POST['user_comment']
            comments.active = False
            comments.save()
            return render(request, 'main/success.html')
    return render(request, 'main/article_details.html', {"article": article, "user_comments": user_comments, "comment_count": comment_count})

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


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        elif user is None:
            return render(request, 'main/login.html', {'error': 'Please contact your Admin to get a account!!'})
    return render(request, 'main/login.html')

def register(request):
    if request.method == 'POST':
        
        if request.POST['password1'] == request.POST['password2']:

            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'main/register.html', {'error': 'Username is Taken!'})

            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                user.is_active = False
                user_info = Profile()
                user_info.staff_level = request.POST['staff_level']
                user_info.name = request.POST['username']
                user.save()
                user_info.save()
                auth.login(request, user)
                return redirect('approval')
        else:
            return render(request, 'main/register.html', {'error': 'Passwords must match!'})

    else:
        return render(request, 'main/register.html')
    return render(request, 'main/register.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def profile(request):
    user = User.objects.get(username=request.user)
    info = Profile.objects.get(user=request.user)
    return render(request, 'main/profile.html', {'info': info, 'user': user})

def approval(request):
    return render(request, 'main/approval.html')

@login_required
def create(request):

    if request.method == 'POST':
        if request.POST['title'] and request.POST['tag'] and request.POST['headline'] and request.POST['content']:
            article = Blog()
            article.user = request.user
            article.title = request.POST['title']
            article.tag = request.POST['tag']
            article.headline = request.POST['headline']
            article.content = request.POST['content']
            article.created_at = timezone.now()
            article.save()
            return render(request, 'main/article_success.html')
    return render(request, 'main/create.html')


def article_success(request):
    return render(request, 'main/article_success.html')