from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog', views.blog, name='blog'),
    path('blog/<int:blog_id>/', views.blog_details, name='blog_details')
]
