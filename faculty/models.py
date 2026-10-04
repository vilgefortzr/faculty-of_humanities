from django.db import models
from django.utils import timezone


class FacultyInfo(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    contacts = models.TextField()

    class Meta:
        verbose_name_plural = "Faculty info"

    def __str__(self):
        return self.title


class Subject(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=80)
    head_of_department = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Major(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    recruiter_name = models.CharField(max_length=80)
    recruiter_phone = models.CharField(max_length=20)
    graduating_department = models.ForeignKey(
        Department, on_delete=models.PROTECT, related_name="majors"
    )
    subjects = models.ManyToManyField(Subject, related_name="majors", blank=True)

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    ACADEMIC_POSITIONS = [
        ("assistant", "Асистент"),
        ("senior_lecturer", "Старший викладач"),
        ("associate_professor", "Доцент"),
        ("professor", "Професор"),
    ]
    ACADEMIC_DEGREES = [
        ("none", "Без ступеня"),
        ("phd", "Доктор філософії"),
        ("dsc", "Доктор наук"),
    ]

    name = models.CharField(max_length=80)
    academic_position = models.CharField(max_length=20, choices=ACADEMIC_POSITIONS)
    academic_degree = models.CharField(
        max_length=20, choices=ACADEMIC_DEGREES, blank=True, default="none"
    )
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, related_name="lecturers"
    )

    def __str__(self):
        return self.name


class ExchangeProgram(models.Model):
    university = models.CharField(max_length=80)
    country = models.CharField(max_length=80, default="")
    languages = models.CharField(max_length=80)
    study_places = models.IntegerField()
    deadline = models.DateField()
    description = models.TextField()

    class Meta:
        ordering = ["deadline"]

    def __str__(self):
        return self.university

    @property
    def deadline_passed(self):
        return self.deadline < timezone.localdate()
