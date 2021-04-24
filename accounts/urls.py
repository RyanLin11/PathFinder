from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('', views.index, name='index'),
]
