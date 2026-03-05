import datetime 
from .forms import TeacherForm
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Teacher, TeacherInfo, Course, Student
from django import forms
from django.contrib import messages



class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'hire_date', 'salary', 'is_active']


class TeacherInfoForm(forms.ModelForm):
    class Meta:
        model = TeacherInfo
        fields = ['phone', 'birth_date', 'passport_number', 'experience_years', 'bio']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'level', 'duration_hours', 'price', 'max_students', 'teacher']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone', 'birth_date', 'is_active']


def teacher_list(request):
    teachers = Teacher.objects.all()
    #запрос: преподаватели без профиля
    teachers_without_info = Teacher.objects.filter(info__isnull=True)

    context = {
        'teachers': teachers,
        'teachers_without_info': teachers_without_info,
    }
    return render(request, 'schedule/teacher_list.html', context)


def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'schedule/teacher_detail.html', {'teacher': teacher})


def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = Teacher.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                hire_date=form.cleaned_data['hire_date'] or datetime.date.today(),
                salary=form.cleaned_data['salary'],
                is_active=form.cleaned_data['is_active']
            )


            TeacherInfo.objects.create(
                teacher=teacher,
                phone=form.cleaned_data.get('phone', ''),
                birth_date=form.cleaned_data.get('birth_date'),
                experience_years=form.cleaned_data.get('experience_years', 0),
                bio=form.cleaned_data.get('bio', '')
            )

            messages.success(request, f'преподаватель {teacher} создан!')
            return redirect('teacher_list')
    else:
        form = TeacherForm()

    return render(request, 'schedule/teacher_form.html', {'form': form})

def teacher_update(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    try:
        teacher_info = teacher.info
    except TeacherInfo.DoesNotExist:
        teacher_info = TeacherInfo.objects.create(teacher=teacher)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        info_form = TeacherInfoForm(request.POST, instance=teacher_info)

        if form.is_valid() and info_form.is_valid():
            form.save()
            info_form.save()
            messages.success(request, 'Данные преподавателя обновлены!')
            return redirect('teacher_detail', teacher_id=teacher.id)
    else:
        form = TeacherForm(instance=teacher)
        info_form = TeacherInfoForm(instance=teacher_info)

    context = {
        'form': form,
        'info_form': info_form,
        'teacher': teacher,
        'title': 'Редактировать преподавателя'
    }
    return render(request, 'schedule/teacher_update.html', context)


def teacher_delete(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == 'POST':
        teacher.delete()
        messages.success(request, 'Преподаватель удален!')
        return redirect('teacher_list')

    return render(request, 'schedule/teacher_confirm_delete.html', {'teacher': teacher})


def course_list(request):
    courses = Course.objects.all()

    #abkmфильто по преподавателю
    teacher_filter = request.GET.get('teacher')
    if teacher_filter:
        courses = courses.filter(teacher_id=teacher_filter)

    #запрос: преподаватели с количеством курсов
    teachers_with_course_count = Teacher.objects.annotate(
        course_count=Count('courses')
    ).filter(course_count__gt=0)

    context = {
        'courses': courses,
        'teachers': Teacher.objects.all(),
        'teachers_with_course_count': teachers_with_course_count,
    }
    return render(request, 'schedule/course_list.html', context)


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, f'Курс "{course.title}" создан!')
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'schedule/course_form.html', {'form': form, 'title': 'Создать курс'})


def course_update(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Курс обновлен!')
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)

    return render(request, 'schedule/course_form.html', {'form': form, 'course': course, 'title': 'Редактировать курс'})


def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Курс удален!')
        return redirect('course_list')

    return render(request, 'schedule/course_confirm_delete.html', {'course': course})




def student_list(request):
    students = Student.objects.all()

    #запрос студенты без курсов
    students_without_courses = Student.objects.filter(courses__isnull=True)

    context = {
        'students': students,
        'students_without_courses': students_without_courses,
    }
    return render(request, 'schedule/student_list.html', context)


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'schedule/student_detail.html', {'student': student})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Студент {student} создан!')
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'schedule/student_form.html', {'form': form, 'title': 'Создать студента'})


def student_update(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные студента обновлены!')
            return redirect('student_detail', student_id=student.id)
    else:
        form = StudentForm(instance=student)

    return render(request, 'schedule/student_form.html',
                  {'form': form, 'student': student, 'title': 'Редактировать студента'})


def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Студент удален!')
        return redirect('student_list')

    return render(request, 'schedule/student_confirm_delete.html', {'student': student})


def enroll_student(request, student_id, course_id):
    student = get_object_or_404(Student, id=student_id)
    course = get_object_or_404(Course, id=course_id)

    student.courses.add(course)
    messages.success(request, f'Студент {student} записан на курс "{course.title}"!')

    return redirect('student_detail', student_id=student.id)


def drop_course(request, student_id, course_id):
    student = get_object_or_404(Student, id=student_id)
    course = get_object_or_404(Course, id=course_id)

    student.courses.remove(course)
    messages.success(request, f'Студент {student} отписан от курса "{course.title}"!')

    return redirect('student_detail', student_id=student.id)



def orm_queries(request):
    #студенты конкретного курса
    course_students = None
    course_id = request.GET.get('course_id')
    if course_id:
        course = get_object_or_404(Course, id=course_id)
        course_students = course.students.all()

    #преподаватели у которых больше N курсов
    teachers_more_than = Teacher.objects.annotate(
        course_count=Count('courses')
    ).filter(course_count__gt=1)  # больше 1 курса

    #Студ без курсов
    students_no_courses = Student.objects.filter(courses__isnull=True)

    #Препод без профиля TeacherInfo
    teachers_no_info = Teacher.objects.filter(info__isnull=True)

    #без студентов
    courses_no_students = Course.objects.annotate(
        student_count=Count('students')
    ).filter(student_count=0)

    context = {
        'course_students': course_students,
        'teachers_more_than': teachers_more_than,
        'students_no_courses': students_no_courses,
        'teachers_no_info': teachers_no_info,
        'courses_no_students': courses_no_students,
        'courses': Course.objects.all(),
    }
    return render(request, 'schedule/orm_queries.html', context)

# Create your views here.
