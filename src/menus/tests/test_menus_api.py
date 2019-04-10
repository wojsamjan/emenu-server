from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from menus.models import Menu
from menus.serializers import MenuSerializer


MENUS_URL = reverse('menus:menu-list')


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
