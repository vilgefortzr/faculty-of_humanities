from django.contrib import admin

from .models import Department, ExchangeProgram, FacultyInfo, Lecturer, Major, Subject

admin.site.register(FacultyInfo)
admin.site.register(Subject)
admin.site.register(Department)
admin.site.register(Major)
admin.site.register(Lecturer)
admin.site.register(ExchangeProgram)
