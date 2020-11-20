from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/', views.logout, name='logout'),
    path('login/', views.register, name='register'),
]
