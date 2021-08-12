from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):  #функция чтоб в админке изменить city object() на название города
        return self.name
    class Meta:  # в админке опять же поменять названия
        verbose_name='Город'
        verbose_name_plural = 'Города'
        ordering = ['name'] # в админке сортировка по алфавиту городов