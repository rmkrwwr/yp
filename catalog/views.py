from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = request.GET.get('name', 'Гость')
    password = request.GET.get('password', 'Не задан')
    return HttpResponse(f"""
    <h1>Стартовая страница</h1>
    <p>Name: {name}</p>
    <p>Password: {password}</p>
    """)

def courses(request):
    courses_list = """
    <h1>Список курсов</h1>
    <ul>
        <li>Python для начинающих</li>
        <li>Django Pro</li>
        <li>Frontend с нуля</li>
    </ul>
    <a href="/">На главную</a>
    """
    return HttpResponse(courses_list)

def course_detail(request, course_id):
    return HttpResponse(f"""
    <h1>Курс #{course_id}</h1>
    <p>Информация о курсе с ID {course_id}</p>
    <a href="/courses/">Назад к курсам</a>
    """)

def authors(request):
    authors_list = """
    <h1>Список авторов</h1>
    <ul>
        <li><a href="/author/1/">Витя Ламба</a></li>
        <li><a href="/author/2/">Андрей Падалко</a></li>
        <li><a href="/author/3/">Семен Мельников</a></li>
    </ul>
    <a href="/">На главную</a>
    """
    return HttpResponse(authors_list)

def author_detail(request, author_id):
    return HttpResponse(f"""
    <h1>Автор #{author_id}</h1>
    <p>Профиль автора с ID {author_id}</p>
    <a href="/authors/">Назад к авторам</a>
    """)
def info(request):
    host = request.META.get("HTTP_HOST", "Не указан")
    user_agent = request.META.get("HTTP_USER_AGENT", "Не указан")
    path = request.path
    method = request.method
    cookies = request.COOKIES

    return HttpResponse(f"""
    <h1>Информация о запросе</h1>
    <p>Host: {host}</p>
    <p>User Agent: {user_agent}</p>
    <p>Path: {path}</p>
    <p>Method: {method}</p>
    <p>Cookies: {cookies}</p>
    <a href="/">На главную</a>
    """)
def not_found(request, exception):
    return HttpResponse(f"""
    <h1>404 - Страница не найдена хахахах</h1>
    <p>Такой страницы не существует</p>
    <p>Ошибка: {exception}</p>
    <a href="/">На главную</a>
    """, status=404)
def test_404(request):
    return HttpResponse("""
    <h1>Тестовая 404 страница</h1>
    <p>Это для проверки</p>
    <a href="/">На главную</a>
    """)