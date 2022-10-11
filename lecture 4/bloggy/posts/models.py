from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)
   
    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    text= models.TextField()
    cdate = models.DateField(auto_now=False)
    visible= models.BooleanField()


class Location(models.Model):
    name = models.TextField()
    
    class Meta:
        db_table = 'ABCDE'

class Shop(models.Model):
    name= models.CharField(max_length=20)
    location = models.ManyToManyField(Location)