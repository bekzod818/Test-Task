from django.db import models


class Employee(models.Model):
    """Сотрудник(Имя, Фамилия, Возраст, Пол, Отдел)"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=20)
    section = models.ForeignKey("Section", on_delete=models.CASCADE)
    lang = models.ForeignKey("ProgLang", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Section(models.Model):
    """Отдел (Название, этаж)"""
    title = models.CharField(max_length=100)
    floor = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class ProgLang(models.Model):
    """Язык программирования(Название)"""
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
