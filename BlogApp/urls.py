from django.urls import path
from . import views

app_name = 'BlogApp'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:blog_id>/', views.post, name='post'),
]
