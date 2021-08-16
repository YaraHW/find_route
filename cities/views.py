from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from cities.models import City
import datetime


def home(request):
    return render(request,"home.html")

def spisok_gorodov(request, pk=None):
    if pk:
        """В общем это функция для вывода списка городов на отдельной странице,
    pk это необязательный аргумент, его приравниваем к записи из бд, если он существует
    то она откроет страницу с данным  городом, типо id=1(pk) (Берлин).
    Есть 3 разных метода как это можно выводить, те что city"""
        # city = City.objects.filter(id=pk).first()
        # city = City.objects.get(id=pk)
        city = get_object_or_404(City, id=pk) # тут он выдаст если есть обьект, если нет выкинет 404
        slovar = {'gorod':city}
        return render(request, 'details.html', slovar)
    qs = City.objects.all()   # queryset, по сути перечисление всех данных из модели City (т.е городов)
    slovar = {'nabor_gorodov':qs}
    return render(request, 'spisok_gorodov.html', slovar)


