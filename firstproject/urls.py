"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http.request import HttpRequest
from django.http.response import HttpResponse

def home_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Home page</h1>")

def progression_page(request: HttpRequest, start: int, count: int, step: int) -> HttpResponse:
    result = [int(start)]
    for i in range(int(count) - 1):
        result.append(result[i] + int(step))
    return HttpResponse(f"<p>{result}</p>")

def fib_page(request:HttpRequest, n: int) -> HttpResponse:
    n = int(n)
    if n <= 0:
        fib_sum = 0
    elif n == 1:
        fib_sum = 1
    else:
        fib1 = 0
        fib2 = 1
        i = 1
        while i < n:
            fib_sum = fib2 + fib1
            fib1 = fib2
            fib2 = fib_sum
            i += 1
    return HttpResponse(f"<h1>{fib_sum}</h1>")

def greeting_page(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f"<h3>Greeting, {name}</h3>")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', home_page),
    path('home/', home_page),
    path('', home_page),
    path('progression/<start>/<count>/<step>', progression_page),
    path('fib/<n>', fib_page),
    path('greeting/<name>', greeting_page)
]
