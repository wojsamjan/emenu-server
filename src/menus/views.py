from rest_framework import viewsets, mixins

from menus.models import Meal, Menu
from menus import serializers


class MealViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    """Manage meals in the database"""
    queryset = Meal.objects.all()
    serializer_class = serializers.MealSerializer
    
    def perform_create(self, serializer):
        """Create a new meal"""
        serializer.save()
        
        
class MenuViewSet(viewsets.ModelViewSet):
    """Manage menus in the database"""
    queryset = Menu.objects.all()
    serializer_class = serializers.MenuSerializer

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'retrieve':
            return serializers.MenuDetailSerializer
    
        return self.serializer_class
