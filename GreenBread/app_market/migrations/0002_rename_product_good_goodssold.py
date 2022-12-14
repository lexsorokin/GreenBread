# Generated by Django 4.1.3 on 2022-11-21 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_categories', '0002_alter_subcategory_options'),
        ('app_market', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Good',
        ),
        migrations.CreateModel(
            name='GoodsSold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold', models.IntegerField(null=True, verbose_name='Продано')),
                ('good', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_market.good', verbose_name='Товар')),
            ],
        ),
    ]
