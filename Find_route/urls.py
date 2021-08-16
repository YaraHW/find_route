"""Find_route URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from cities.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('spisok_gorodov/', spisok_gorodov, name='spisok_gorodov'),
    path('spisok_gorodov/<int:pk>/', spisok_gorodov), # int:pk - инт это номер записи из БД, а pk это параметр ф-ии spisok_gorodov, если запись с таким id есть то он отобразит
    path('spisok_gorodov/details/', spisok_gorodov),
    re_path(r'^$', home, name='home'), # это та же стартовая страница, но с использованием функции re_path. Ее используют когда применяют регулярные выражения. (r'^$' - означает пустую строку, т.е ссылка в корень сайта)

]