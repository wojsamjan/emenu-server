from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from menus.models import Menu, Meal
from menus.serializers import MenuSerializer, MenuDetailSerializer


MENUS_URL = reverse('menus:menu-list')


def detail_url(menu_id):
    """Return menu detail URL"""
    return reverse('menus:menu-detail', args=[menu_id])


def create_meal(name='meal', description='meal', price=1.99, time_minutes=30):
    return Meal.objects.create(name=name, description=description, price=price, time_minutes=time_minutes)


def create_menu(name='menu', description='menu'):
    return Menu.objects.create(name=name, description=description)


class MenusApiTests(TestCase):
    """Test the menus API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_menus(self):
        """Test retrieving a list of menus"""
        create_menu(name='first menu')
        create_menu(name='second menu')

        res = self.client.get(MENUS_URL)

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        
    def test_view_menu_detail(self):
        """Test viewing a menu detail"""
        menu = create_menu()
        menu.meals.add(create_meal())

        url = detail_url(menu.id)
        res = self.client.get(url)

        serializer = MenuDetailSerializer(menu)
        self.assertEqual(res.data, serializer.data)

    def test_create_menu_successful(self):
        """Test creating a new menu"""
        payload = {
            'name': 'Test menu name',
            'description': 'Test menu description'
        }
        res = self.client.post(MENUS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        menu = Menu.objects.get(id=res.data['id'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(menu, key))

    def test_create_menu_invalid(self):
        """Test creating a new menu with invalid payload"""
        payload = {
            'name': '',
            'description': 'Test menu description'
        }
        res = self.client.post(MENUS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_create_menu_not_unique(self):
        """Test creating a new menu with not unique name"""
        payload = {
            'name': 'unique name',
            'description': 'description'
        }
        self.client.post(MENUS_URL, payload)
        res = self.client.post(MENUS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_menu_with_meals(self):
        """Test creating a menu with meals"""
        meal1 = create_meal(name='1st meal')
        meal2 = create_meal(name='2nd meal')
        payload = {
            'name': 'Test menu name',
            'description': 'Test menu description',
            'meals': [meal1.id, meal2.id]
        }
        res = self.client.post(MENUS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        menu = Menu.objects.get(id=res.data['id'])
        meals = menu.meals.all()
        self.assertEqual(meals.count(), 2)
        self.assertIn(meal1, meals)
        self.assertIn(meal2, meals)
