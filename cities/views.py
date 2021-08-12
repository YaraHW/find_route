from django.shortcuts import render

from cities.models import City


def home(request):
    return render(request,"home.html")

def spisok_gorodov(request):
    qs = City.objects.all()   # queryset, по сути перечисление всех данных из модели City (т.е городов)
    slovar = {'objects_list':qs}
    return render(request, 'spisok_gorodov.html', slovar)