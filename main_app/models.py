from datetime import date
from email.mime import image
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'main_app/static/uploads/', default="")
    upload_image_of_ingredients = models.ImageField(upload_to = 'main_app/static/uploads/', default="")
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    ingredients = models.CharField(max_length=300, default="")
    method = models.CharField(max_length=300, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user id? 


    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs = {'recipe_id': self.id })

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default="")
    allergy = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredients_detail', kwargs={'pk': self.id})

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'main_app/static/uploads/', default="")

# USER SPECIFIC
class CustomIngredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default="")
    allergy = models.CharField(max_length=100)
    




