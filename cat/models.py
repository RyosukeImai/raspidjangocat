from django.db import models
from django.utils import timezone   # Django ではdatetime.nnow の代わりに使う

class Cat(models.Model):
    name = models.CharField('名前',max_length=100)
    text = models.TextField('本文')
    date = models.DateTimeField('登録日付',default=timezone.now)

