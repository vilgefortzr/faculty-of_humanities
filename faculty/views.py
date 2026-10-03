from django.shortcuts import render, get_object_or_404
from .models import FacultyInfo, Major


def home(request):
    faculty_info = FacultyInfo.objects.first()
    return render(request, 'faculty/home.html', {'faculty_info': faculty_info})


def programs(request):
    majors = Major.objects.all()
    return render(request, 'faculty/programs.html', {'majors': majors})


def major(request, major_id):
    program = get_object_or_404(Major, id=major_id)
    subjects = program.subjects.all()
    return render(request, 'faculty/major.html', {'major': program, 'subjects': subjects})


def departments(request):
    return render(request, 'faculty/departments.html')
