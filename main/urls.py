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
]
