from django.shortcuts import render
from django.http import HttpResponse

COURSES = [
    {'id': 1, 'title': 'Python для начинающих', 'description': 'Основы Python'},
    {'id': 2, 'title': 'Django Pro', 'description': 'Веб-разработка на Django'},
    {'id': 3, 'title': 'Frontend с нуля', 'description': 'HTML, CSS, JavaScript'},
]

AUTHORS = [
    {'id': 1, 'name': 'Витя Ламба', 'bio': 'Python разработчик'},
    {'id': 2, 'name': 'Андрей Падалко', 'bio': 'Django разработчик'},
    {'id': 3, 'name': 'Семен Мельников', 'bio': 'Frontend разработчик'},
]

def index(request):
    name = request.GET.get('name', 'Гость')
    password = request.GET.get('password', 'Не задан')

    context = {
        'name': name,
        'password': password,
        'courses_count': len(COURSES),
        'authors_count': len(AUTHORS),
    }
    return render(request, 'index.html', context)

def courses(request):
    context = {
        'courses': COURSES,
    }
    return render(request, 'courses.html', context)

def course_detail(request, course_id):
    course = next((c for c in COURSES if c['id'] == course_id), None)

    if not course:
        return render(request, 'not_found.html', status=404)

    context = {
        'course': course,
    }
    return render(request, 'course_detail.html', context)

def authors(request):
    context = {
        'authors': AUTHORS,
    }
    return render(request, 'authors.html', context)

def author_detail(request, author_id):
    author = next((a for a in AUTHORS if a['id'] == author_id), None)

    if not author:
        return render(request, 'not_found.html', status=404)

    context = {
        'author': author,
    }
    return render(request, 'author_detail.html', context)

def info(request):
    context = {
        'host': request.META.get("HTTP_HOST", "Не указан"),
        'user_agent': request.META.get("HTTP_USER_AGENT", "Не указан"),
        'path': request.path,
        'method': request.method,
        'cookies': request.COOKIES,
        'get_params': request.GET,
    }
    return render(request, 'info.html', context)

def not_found(request, exception=None):
    return render(request, 'not_found.html', status=404)