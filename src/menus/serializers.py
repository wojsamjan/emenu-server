from rest_framework import serializers

from menus.models import Meal, Menu


class MealSerializer(serializers.ModelSerializer):
    """Serializer for meal objects"""

    class Meta:
        model = Meal
        fields = ('id', 'name', 'description', 'price', 'time_minutes', 'is_vegan', 'created_date', 'modified_date')
        read_only_fields = ('id', 'created_date', 'modified_date')
        
        
class MenuSerializer(serializers.ModelSerializer):
    """Serialize a menu"""
    
    meals = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Meal.objects.all()
    )
    
    class Meta:
        model = Menu
        fields = ('id', 'name', 'description', 'created_date', 'modified_date', 'meals')
        read_only_fields = ('id', 'created_date', 'modified_date')
