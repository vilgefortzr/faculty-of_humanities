from django.shortcuts import get_object_or_404, render

from .models import Department, ExchangeProgram, FacultyInfo, Major


def home(request):
    faculty_info = FacultyInfo.objects.first()
    return render(request, "faculty/home.html", {"faculty_info": faculty_info})


def programs(request):
    majors = Major.objects.all()
    return render(request, "faculty/programs.html", {"majors": majors})


def major(request, major_id):
    program = get_object_or_404(Major, id=major_id)
    subjects = program.subjects.all()
    return render(
        request, "faculty/major.html", {"major": program, "subjects": subjects}
    )


def departments(request):
    departments_list = Department.objects.all()
    return render(
        request, "faculty/departments.html", {"departments": departments_list}
    )


def department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    lecturers = department.lecturers.all()
    return render(
        request,
        "faculty/department.html",
        {"department": department, "lecturers": lecturers},
    )


def exchange(request):
    exchange_program = ExchangeProgram.objects.all()
    return render(request, "faculty/exchange.html", {"exchange": exchange_program})
