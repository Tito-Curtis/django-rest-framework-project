from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Color(models.Model):
    color_name = models.CharField(max_length=100)
    def __str__(self):
        return self.color_name