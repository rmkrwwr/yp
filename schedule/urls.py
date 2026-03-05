from django.urls import path
from . import views

urlpatterns = [

    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teacher/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    path('teacher/create/', views.teacher_create, name='teacher_create'),
    path('teacher/<int:teacher_id>/update/', views.teacher_update, name='teacher_update'),
    path('teacher/<int:teacher_id>/delete/', views.teacher_delete, name='teacher_delete'),


    path('courses/', views.course_list, name='course_list'),
    path('course/create/', views.course_create, name='course_create'),
    path('course/<int:course_id>/update/', views.course_update, name='course_update'),
    path('course/<int:course_id>/delete/', views.course_delete, name='course_delete'),


    path('students/', views.student_list, name='student_list'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('student/create/', views.student_create, name='student_create'),
    path('student/<int:student_id>/update/', views.student_update, name='student_update'),
    path('student/<int:student_id>/delete/', views.student_delete, name='student_delete'),
    path('student/<int:student_id>/enroll/<int:course_id>/', views.enroll_student, name='enroll_student'),
    path('student/<int:student_id>/drop/<int:course_id>/', views.drop_course, name='drop_course'),


    path('orm-queries/', views.orm_queries, name='orm_queries'),
]