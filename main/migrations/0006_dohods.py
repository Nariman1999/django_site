# Generated by Django 4.1.3 on 2022-12-14 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_novosti_image_novosti_image0_novosti_image1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dohods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата публикации')),
                ('otkogo', models.CharField(max_length=300)),
                ('summa', models.IntegerField()),
            ],
        ),
    ]
