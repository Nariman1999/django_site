# Generated by Django 4.1.3 on 2022-12-18 19:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_article_date_alter_document_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='novosti',
            name='title',
            field=models.CharField(default='Заголовок', max_length=200, verbose_name='Заголовок '),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 12, 19, 1, 41, 27, 510136), verbose_name='Дата '),
        ),
    ]
