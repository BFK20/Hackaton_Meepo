from django.db import models

# Create your models here.

class vuses(models.Model):
    title = models.CharField('Название Вуза', max_length=100)  # текст до 255 символов
    task = models.TextField('Описание')  # колво символов не ограничено

    def __str__(self):
        return self.title
