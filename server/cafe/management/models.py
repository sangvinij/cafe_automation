from django.db import models


class Menu(models.Model):
    title = models.CharField('title', max_length=255, null=False)
    price = models.FloatField('price', null=False)
    image = models.ImageField('image')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        unique_together = ('title', 'category')


class Category(models.Model):
    category_name = models.CharField('category_name', max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class CafeAddresses(models.Model):
    cafe_address = models.CharField('address', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class SocialMediaLinks(models.Model):
    social_media_name = models.CharField(max_length=255)
    social_media_link = models.URLField()

    class Meta:
        unique_together = ('social_media_name', 'social_media_link')
