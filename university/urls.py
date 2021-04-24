from django.urls import path, include
from . import views

app_name = 'university'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.uniprofile, name='uniprofile'),
    path('program/<int:pk>', views.program, name='program'),
]
