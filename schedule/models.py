from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(unique=True, verbose_name="Email")
    hire_date = models.DateField(default=datetime.date.today, verbose_name="Дата найма")
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


# 1:1
class TeacherInfo(models.Model):
    teacher = models.OneToOneField(
        Teacher,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='info'
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    passport_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
    experience_years = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    bio = models.TextField(blank=True, verbose_name="Биография")

    def __str__(self):
        return f"Info: {self.teacher.last_name}"

    class Meta:
        verbose_name = "Информация о преподавателе"


# N:1 с препод
class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Начальный'),
        ('intermediate', 'Средний'),
        ('advanced', 'Продвинутый'),
    ]

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='courses',
        verbose_name="Преподаватель"
    )
    title = models.CharField(max_length=200, unique=True, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    duration_hours = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    max_students = models.IntegerField(default=30, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


# (N:N с курсм
class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    enrollment_date = models.DateField(auto_now_add=True, verbose_name="Дата зачисления")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    courses = models.ManyToManyField(Course, related_name='students', blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

# Create your models here.


#1:1	Teacher ↔ TeacherInfo	OneToOneField
#1:N	Teacher → Course	ForeignKey в Course
#N:N	Student ↔ Course	ManyToManyField
