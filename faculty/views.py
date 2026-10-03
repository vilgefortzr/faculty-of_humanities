from django.shortcuts import render


def home(request):
    return render(request, 'faculty/home.html')


def programs(request):
    return render(request, 'faculty/programs.html')


def departments(request):
    return render(request, 'faculty/departments.html')
