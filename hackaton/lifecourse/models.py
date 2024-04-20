from django.db import models

# Create your models here.

class vuses(models.Model):
    name = models.CharField('Название Вуза', max_length=100)  # текст до 255 символов

    def __str__(self):
        return self.vusname

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(vuses, on_delete=models.CASCADE)

class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)



class Student(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(vuses, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


