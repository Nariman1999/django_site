from django.db import models
from datetime import datetime

class People(models.Model):
    name = models.CharField(max_length = 120, verbose_name = "ФИО ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Члены фонда  "
        verbose_name_plural = "Члены фонда (ФИО)  "

class Article(models.Model):
    name = models.ForeignKey(People, on_delete = models.CASCADE, verbose_name = "ФИО ")
    sdal = models.IntegerField(verbose_name = "Сдал ")
    ostatok = models.IntegerField(verbose_name = "Остаток ",default=2400)
    date = models.DateField(verbose_name = "Дата ",default = datetime.now(), blank = True)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ''.join(field_values[1])+' --- ' + ''.join(field_values[4])
    class Meta:
        verbose_name = "Общий фонд"
        verbose_name_plural = "Общий фонд "

class Novosti(models.Model):
    date_time = models.DateTimeField('Дата публикации')
    title = models.CharField('Заголовок ', default=" ",max_length = 200) 
    text = models.TextField('Текст')
    image0 = models.ImageField('Фото 1', null=True, blank=True,  upload_to='novost_file')
    image1 = models.ImageField('Фото 2', null=True, blank=True,  upload_to='novost_file')
    image2 = models.ImageField('Фото 3', null=True, blank=True,  upload_to='novost_file')
    image3 = models.ImageField('Фото 4', null=True, blank=True,  upload_to='novost_file')
    image4 = models.ImageField('Фото 5', null=True, blank=True,  upload_to='novost_file')
    image5 = models.ImageField('Фото 6', null=True, blank=True,  upload_to='novost_file')
    image6 = models.ImageField('Фото 7', null=True, blank=True,  upload_to='novost_file')
    image7 = models.ImageField('Фото 8', null=True, blank=True,  upload_to='novost_file')
    image8 = models.ImageField('Фото 9', null=True, blank=True,  upload_to='novost_file')
    image9 = models.ImageField('Фото 10', null=True, blank=True,  upload_to='novost_file')

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ''.join(field_values[2])+' , ' + ''.join(field_values[1])
    class Meta:
        verbose_name = "Новости "
        verbose_name_plural = "Новости "

class Document(models.Model):
    date_time = models.DateField('Дата публикации') 
    text = models.TextField('Текст')
    files = models.FileField('Документ')
    boolens = models.BooleanField('Видимость ', default = True )

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ''.join(field_values[2])+' , ' + ''.join(field_values[1]) + " " +''.join(field_values[4])
    class Meta:
        verbose_name = "Документы "
        verbose_name_plural = "Документы "


class Dohods(models.Model):
    date = models.DateField('Дата публикации ')
    otkogo = models.CharField('От кого ', max_length = 300)
    summa = models.IntegerField('Сумма ')
    
    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ''.join(field_values[2])+' , ' + ''.join(field_values[1])
    
    class Meta:
        verbose_name = "Доходы "
        verbose_name_plural = "Доходы "


class Rashods(models.Model):
    date = models.DateField('Дата публикации: ')
    rashod = models.CharField('Расход: ',max_length = 300)
    summr = models.IntegerField('Сумма: ')
    

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ''.join(field_values[2])+' , ' + ''.join(field_values[1])
    class Meta:
        verbose_name = "Расходы"
        verbose_name_plural = "Расходы "
