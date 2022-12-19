from django.contrib import admin
from . import models

admin.site.register(models.Article),
admin.site.register(models.Novosti),
admin.site.register(models.Document),
admin.site.register(models.Dohods),
admin.site.register(models.Rashods),
admin.site.register(models.People)