from rest_framework import serializers

from menus.models import Meal


class MealSerializer(serializers.ModelSerializer):
    """Serializer for meal objects"""

    class Meta:
        model = Meal
        fields = ('id', 'name', 'description', 'price', 'time_minutes', 'is_vegan', 'created_date', 'modified_date')
        read_only_fields = ('id', 'created_date', 'modified_date')
