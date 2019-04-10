from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from menus.models import Meal

from menus.serializers import MealSerializer


MEALS_URL = reverse('menus:meal-list')


def create_meal(name='meal', description='meal', price=1.99, time_minutes=30):
    return Meal.objects.create(name=name, description=description, price=price, time_minutes=time_minutes)


class MealsApiTests(TestCase):
    """Test the meals API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_meals(self):
        """Test retrieving meals"""
        create_meal(name='first meal')
        create_meal(name='second meal')

        res = self.client.get(MEALS_URL)

        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
