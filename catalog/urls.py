from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('authors/', views.authors, name='authors'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('info/', views.info, name='info'),
    re_path(r'^about/$', views.info, name='about'),
    path('site/<str:company>/<int:year>/', views.info, name='site_info'),
]