from django.db import models


class Menu(models.Model):
    title = models.CharField('Название', max_length=255)
    price = models.FloatField('Цена')
    image = models.ImageField('Изображение')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Category(models.Model):
    name = models.CharField('Категория', max_length=255, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
