from django.shortcuts import render
from .models import FacultyInfo


def home(request):
    faculty_info = FacultyInfo.objects.first()
    return render(request, 'faculty/home.html', {'faculty_info': faculty_info})


def programs(request):
    return render(request, 'faculty/programs.html')


def departments(request):
    return render(request, 'faculty/departments.html')
