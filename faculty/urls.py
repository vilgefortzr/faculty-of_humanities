from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('programs/', views.programs, name='programs'),
    path('departments/', views.departments, name='departments'),
    path('programs/<int:major_id>/', views.major, name='major'),
    path('departments/<int:department_id>/', views.department, name='department')
]
