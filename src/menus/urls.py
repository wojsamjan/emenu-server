from django.urls import path, include
from rest_framework.routers import DefaultRouter

from menus import views


router = DefaultRouter()
router.register('meals', views.MealViewSet)

app_name = 'menus'

urlpatterns = [
    path('', include(router.urls)),
]
