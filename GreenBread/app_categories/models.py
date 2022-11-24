from django.db import models


class Category(models.Model):
    title = models.CharField(verbose_name='Наименование', null=True, max_length=150)
    index = models.IntegerField(verbose_name='Индекс', null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    title = models.CharField(verbose_name='Подкатегория', null=True, max_length=150)
    index = models.IntegerField(verbose_name='Индекс', null=True)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


