from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Breed(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        '''Добавляем строковое отображение'''
        return f' {self.name}'

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'
        ordering = ['name',]

class Dog(models.Model):
    name = models.CharField(max_length=50, verbose_name='Кличка')
    #breed = models.CharField(max_length=50, verbose_name='Порода', **NULLABLE)
    # заменяем эту строчку согласно решения:
    breed = models.ForeignKey(Breed, related_name="dogs", on_delete=models.CASCADE, verbose_name='Порода')
    image = models.ImageField(upload_to="dogs_image", verbose_name='Фото', **NULLABLE)
    birth_day = models.DateField(verbose_name='Дата рождения', **NULLABLE)

    def __str__(self):
        '''Добавляем строковое отображение'''
        return f' {self.name} ({self.breed})'

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'
        ordering = ['name', 'breed',]
