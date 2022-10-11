from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    
class Comment(models.Model):
    text= models.TextField()
    cdate = models.DateField(auto_now=False)
    visible= models.BooleanField()

class Category(models.Model):
    title = models.CharField(max_length=20)