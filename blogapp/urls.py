from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.register_user, name='register_user'),
    path('blog/', views.create_blog, name='create_blog'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.update_blog, name='update_blog'),
    path('blog/<int:pk>/', views.delete_blog, name='delete_blog'),
    path('user/', views.update_user_profile, name='update_user'),
]