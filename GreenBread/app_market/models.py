from django.db import models


class Good(models.Model):

    STATUS_CHOICES = [
        ('g', 'generic'),
        ('d', 'discount'),
    ]

    title = models.CharField(verbose_name='Наименование', null=True, max_length=150)
    description = models.TextField(verbose_name='Описание', null=True, max_length=1500)
    category = models.ForeignKey('app_categories.Category', verbose_name='Категория', null=True, on_delete=models.CASCADE)
    subcategory = models.ForeignKey('app_categories.Subcategory', verbose_name='Подкатегория', null=True, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена', null=True)
    weight = models.IntegerField(verbose_name='Вес', null=True)
    protein = models.IntegerField(verbose_name='Белки', null=True, help_text='на 100 грамм')
    carbs = models.IntegerField(verbose_name='Углеводы', null=True, help_text='на 100 грамм')
    fats = models.IntegerField(verbose_name='Жиры', null=True, help_text='на 100 грамм')
    ingredients = models.TextField(verbose_name='Ингридиенты', null=True)
    status = models.CharField(verbose_name='Статус', max_length=1, choices=STATUS_CHOICES, default='g')
    expiration_period = models.IntegerField(verbose_name='Срок годности', null=True)
    creation_date = models.DateField(verbose_name='Дата создания', null=True, auto_now_add=True)
    update_date = models.DateField(verbose_name='Дата обновления', null=True, auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class GoodsSold(models.Model):
    good = models.ForeignKey('Good', verbose_name='Товар', null=True, on_delete=models.CASCADE)
    sold = models.IntegerField(verbose_name='Продано', default=0)

    class Meta:
        verbose_name = 'Продано товара'
        verbose_name_plural = 'Продано товаров'
