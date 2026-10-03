from django.contrib import admin

from .models import FacultyInfo, Subject, Department, Major, Lecturer

admin.site.register(FacultyInfo)
admin.site.register(Subject)
admin.site.register(Department)
admin.site.register(Major)
admin.site.register(Lecturer)
