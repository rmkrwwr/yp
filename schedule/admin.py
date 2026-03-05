from django.contrib import admin
from .models import Teacher, TeacherInfo, Course, Student

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_name', 'first_name', 'email', 'is_active']
    list_filter = ['is_active']

@admin.register(TeacherInfo)
class TeacherInfoAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'phone', 'experience_years']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'teacher', 'level', 'price']
    list_filter = ['level', 'teacher']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'email', 'is_active']
    filter_horizontal = ['courses']

# Register your models here.
