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

    def test_create_meal_successful(self):
        """Test creating a new meal"""
        payload = {
            'name': 'Test meal name',
            'description': 'Test meal description',
            'price': 4.95,
            'time_minutes': 45
        }
        self.client.post(MEALS_URL, payload)

        exists = Meal.objects.filter(
            name=payload['name']
        ).exists()
        self.assertTrue(exists)

    def test_create_meal_invalid(self):
        """Test creating a new meal with invalid payload"""
        payload = {
            'name': '',
            'description': 'Test meal description',
            'price': 4.95,
            'time_minutes': 45
        }
        res = self.client.post(MEALS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
