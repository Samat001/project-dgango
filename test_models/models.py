import uuid
from django.db import models


class Category(models.Model): # табличка
    title = models.CharField(max_length=50, unique=True) #атрибут = поле 


class Product(models.Model):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(
        'Category', 
        on_delete=models.CASCADE,
        related_name='products'
    
    )


class Passport(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.TextField()
    

class Person(models.Model):
    name = models.CharField(max_length=50)
    Passport = models.OneToOneField(Passport,on_delete=models.CASCADE, related_name='person')


class Student(models.Model):
    email = models.EmailField()

class Teacher(models.Model):
    email = models.EmailField()
    student = models.ManyToManyField(Student)
