from django.urls import path
from . import views

urlpatterns = [
    path('POST/user/', views.register_user, name='register_user'),
    path('POST/blog/', views.create_blog, name='create_blog'),
    path('GET/blog/', views.blog_list, name='blog_list'),
    path('PUT/blog/<int:pk>/', views.update_blog, name='update_blog'),
    path('DELETE/blog/<int:pk>/', views.delete_blog, name='delete_blog'),
    path('PUT/user/', views.update_user_profile, name='update_user'),
]