from django.db import models

# Create your models here.

class vuses(models.Model):
    vusname = models.CharField('Название Вуза', max_length=100)  # текст до 255 символов
    structure = models.JSONField('Структура', default = '[]')

    def __str__(self):
        return self.title
