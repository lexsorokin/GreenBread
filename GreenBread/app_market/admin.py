from django.contrib import admin

from app_market.models import Good, GoodsSold


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'creation_date', 'expiration_period']


@admin.register(GoodsSold)
class GoodsSoldAdmin(admin.ModelAdmin):
    list_display = ['good', 'sold']
