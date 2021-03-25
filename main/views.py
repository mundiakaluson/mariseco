from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Contact, WebContent, Comment, Profile
from django.utils import timezone
from .forms import CommentForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

def index(request):
    web_content = get_object_or_404(WebContent)
    return render(request, 'main/index.html', {"web_content": web_content})

def blog(request):
    articles = Blog.objects.filter(published=True)
    return render(request, 'main/blog.html', {"articles": articles})

def article_details(request, blog_id):
    article = get_object_or_404(Blog, pk=blog_id)
    comment_count = article.comments.filter(active=True).count()
    approved_comments = article.comments.filter(active=True)
    if request.method == 'POST':
        if request.POST['user_name'] and request.POST['user_email'] and request.POST['user_comment']:
            comments = Comment()
            comments.name = request.POST['user_name']
            comments.blog = article
            comments.created_on = timezone.now()
            comments.email = request.POST['user_email']
            comments.comment = request.POST['user_comment']
            comments.active = False
            comments.save()
            print("[200] Comment Posted and Disabled")
            return render(request, 'main/comment_success.html', {"article": article, "comment_count": comment_count, "approved_comments": approved_comments})
    return render(request, 'main/article_details.html', {"article": article, "comment_count": comment_count, "approved_comments": approved_comments})


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

@login_required
def profile(request):
    user = User.objects.get(username=request.user)
    info = Profile.objects.get(user=request.user)
    return render(request, 'main/profile.html', {'info': info, 'user': user})

def edit_profile(request):
    info = Profile.objects.get(user=request.user)
    return render(request, 'main/edit_profile.html', {'info': info})

def update_profile(request):
    info = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        if request.POST['update_name'] and request.POST['update_email']:
            update_user = User.objects.get(username=request.user)
            update_user.username = request.POST['update_name']
            update_user.email = request.POST['update_email']
            update_user.save()
            return render(request, 'main/profile.html', {'success': 'Profile Update Sucessfully!'})
    return render(request, 'main/profile.html', {'info': info})

def approval(request):
    return render(request, 'main/approval.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['tag'] and request.POST['headline'] and request.POST['content']:
            article = Blog()
            article.author = request.user
            article.title = request.POST['title']
            article.tag = request.POST['tag']
            article.headline = request.POST['headline']
            article.content = request.POST['content']
            article.created_at = timezone.now()
            article.active = False
            article.save()
            return render(request, 'main/article_success.html')
    return render(request, 'main/create.html')

@login_required
def article_success(request):
    return render(request, 'main/article_success.html')

@login_required
def delete(request, username):
    context = {}

    try:
        user = User.objects.get(username=username) 
        user.delete()
        user.save()
        context['deletion_message'] = 'User deleted successfully!'
        return render(request, 'main/delete_or_deactivate_success.html')
    except User.DoesNotExist:
        context['error_message'] = 'User does not exist!!!'

    return render(request, 'main/profile.html', context=context)

@login_required
def deactivate(request, username):
    context = {}

    try:
        user = User.objects.get(username=username)
        user.is_active = False
        user.save()
        context['deactivation_message'] = 'Account Deactivated Successfully!'
        return render(request, 'main/delete_or_deactivate_success.html')
    except User.DoesNotExist:
        context['error_message'] = 'User does not exist!!!'
    return render(request, 'main/profile.html', context=context)

@login_required
def all_staff(request):
    users = get_user_model().objects.all()
    user_count = User.objects.all().count()
    return render(request, 'main/all_staff.html', {'users': users, 'user_count': user_count})

@login_required
def delete_or_deactivate_success(request):
    return render(request, 'main/delete_or_deactivate_success.html')

def control_panel(request):
    contacts = Contact.objects.all()
    users = get_user_model().objects.all()
    user_count = User.objects.all().count()
    pending_comments = Comment.objects.all().filter(active=False)
    comment_count = pending_comments.count()
    return render(request, 'main/control_panel.html', {'users': users, 'user_count': user_count, 'comment_count': comment_count, 'pending_comments': pending_comments, 'contacts': contacts})

def update_web_content(request):
    contacts = Contact.objects.all()
    web_content = WebContent.objects.get(id=1)
    users = get_user_model().objects.all()
    user_count = User.objects.all().count()
    pending_comments = Comment.objects.all().filter(active=False)
    comment_count = pending_comments.count()
    if request.method == 'POST':
        if request.POST['principles'] and request.POST['location'] and request.POST['mission'] and request.POST['form_one_stream'] and request.POST['form_two_stream'] and request.POST['form_three_stream'] and request.POST['form_four_stream'] and request.POST['bom_message']:
            web_content.principles = request.POST['principles']
            web_content.location = request.POST['location']
            web_content.mission = request.POST['mission']
            web_content.form_one_stream = request.POST['form_one_stream']
            web_content.form_two_stream = request.POST['form_two_stream']
            web_content.form_three_stream = request.POST['form_three_stream']
            web_content.form_four_stream = request.POST['form_four_stream']
            web_content.bom_message = request.POST['bom_message']
            web_content.save()
            messages.success(request, 'Web Content Changed Successfully!', extra_tags='alert')
            return render(request, 'main/control_panel.html', {'users': users, 'user_count': user_count, 'comment_count': comment_count, 'pending_comments': pending_comments, 'contacts': contacts})
    return render(request, 'main/control_panel.html', {'users': users, 'user_count': user_count, 'comment_count': comment_count, 'pending_comments': pending_comments, 'contacts': contacts})


