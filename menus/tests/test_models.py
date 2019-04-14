from django.test import TestCase

from menus.models import Menu, Meal


def create_meal(name='meal', description='meal', price=1.99, time_minutes=30):
    return Meal.objects.create(
        name=name, description=description, price=price, time_minutes=time_minutes
    )


def create_menu(name='menu', description='menu'):
    return Menu.objects.create(name=name, description=description)


class MealTests(TestCase):
    
    def test_meal_str(self):
        """Test the meal string representation"""
        meal = create_meal()

        self.assertTrue(isinstance(meal, Meal))
        self.assertEqual(str(meal), meal.name)


class MenuTests(TestCase):

    def test_menu_str(self):
        """Test the menu string representation"""
        menu = create_menu()

        self.assertTrue(isinstance(menu, Menu))
        self.assertEqual(str(menu), menu.name)
