import uuid
import os

from django.db import models


def meal_image_file_path(instance, filename):
    """Generate file path for new meal image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/meal/', filename)


class Meal(models.Model):
    """Meal to be used in a menu"""
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    time_minutes = models.IntegerField()
    is_vegan = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, upload_to=meal_image_file_path)

    def __str__(self):
        return self.name


class Menu(models.Model):
    """Menu object"""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    meals = models.ManyToManyField('Meal', related_name='menus')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
