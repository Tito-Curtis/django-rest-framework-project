from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    color = models.ForeignKey('Color', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Color(models.Model):
    color_name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.color_name
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100000)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="post")

    def __str__(self):
        return self.title
