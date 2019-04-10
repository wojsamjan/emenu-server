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
