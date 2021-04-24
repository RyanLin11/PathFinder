from django.shortcuts import render
from .models import University, Program

# Create your views here.
def index(request):
    university_list = University.objects.all()
    return render(request, 'university/index.html', {'university_list':university_list})

def uniprofile(request, pk):
    university = University.objects.get(pk=pk)
    try: 
        programs = Program.objects.filter(university=university)
    except University.DoesNotExist:
        programs = None
    return render(request, 'university/uniprofile.html', {'university':university, 'programs':programs})

def program(request, pk):
    program = Program.objects.get(pk=pk)
    return render(request, 'university/program.html', {'program':program})