from rest_framework import viewsets, mixins

from menus.models import Meal
from menus import serializers


class MealViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage meals in the database"""
    queryset = Meal.objects.all()
    serializer_class = serializers.MealSerializer
