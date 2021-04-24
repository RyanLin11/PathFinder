from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile
#from university.models import Course
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ChangeUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-user', 'placeholder':'Email Address'}))
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email']
'''
class ChangeCourseForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all())
    class Meta:
        model = User
        fields = ['courses']
'''
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-user', 'placeholder':'Password'}))

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-user', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-user', 'placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-user', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-user', 'placeholder':'Re-enter Password'}))
    class Meta:
        model = User
        fields = ['username', 'email']