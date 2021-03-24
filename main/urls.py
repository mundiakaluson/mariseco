from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog', views.blog, name='blog'),
    path('article_details/<int:blog_id>/', views.article_details, name='article_details'),
    path('covid_stats', views.covid_stats, name='covid_stats'),
    path('contact', views.contact, name='contact'),
    path('success', views.success, name='success'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('register', views.register, name='register'),
    path('approval', views.approval, name='approval'),
    path('create', views.create, name='create'), 
    path('article_success', views.article_success, name='article_success'),
    path('delete/<str:username>/', views.delete, name='delete'),
    path('delete_or_deactivate_success', views.delete_or_deactivate_success, name='delete_or_deactivate_success'),
    path('deactivate/<str:username>/', views.deactivate, name='deactivate'),
    path('all_staff', views.all_staff, name='all_staff'),
]
