from django.db import models
from django.forms import CharField

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
    
class Country(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Capital(models.Model):
    name = models.CharField(max_length=30,null=False,)
    country = models.OneToOneField(to='Country',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    name=models.CharField(max_length=30)
    country = models.ForeignKey(to=Country,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.first_name
    
class Subject(models.Model):
    title = models.CharField(max_length=20)
    teachers = models.ManyToManyField(Teacher)
    
    def __str__(self):
        return self.title