from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
