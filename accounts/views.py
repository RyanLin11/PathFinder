from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    else:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            print(form.is_valid())
            if form.is_valid():
                form.save()
                return redirect('accounts:login')
        context = {'form':form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    else:
        form = LoginForm()
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts:index')
        context = {'form':form}
        return render(request, 'accounts/login.html', context)

@login_required(login_url='accounts:login')
def logoutUser(request):
    logout(request)
    return redirect('accounts:login')