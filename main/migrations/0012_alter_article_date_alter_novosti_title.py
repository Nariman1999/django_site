# Generated by Django 4.1.3 on 2022-12-18 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_novosti_title_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 12, 19, 1, 42, 45, 961302), verbose_name='Дата '),
        ),
        migrations.AlterField(
            model_name='novosti',
            name='title',
            field=models.CharField(default=' ', max_length=200, verbose_name='Заголовок '),
        ),
    ]
