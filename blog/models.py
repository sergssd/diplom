from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, unique=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    price = models.IntegerField()


    def __str__(self):
        return self.name
