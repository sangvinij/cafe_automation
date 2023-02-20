# Generated by Django 4.1.7 on 2023-02-20 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_alter_menu_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='category_name'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.FloatField(verbose_name='price'),
        ),
    ]