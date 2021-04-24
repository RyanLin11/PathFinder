from django.forms import modelform_factory
from .models import Application, Program
from django import forms
from django.contrib.auth.models import User

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['status', 'program', 'grade', 'user']
