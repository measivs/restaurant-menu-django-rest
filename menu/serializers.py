from rest_framework import serializers
from .models import MenuCategory, SubMenuCategory, Dish, Ingredient
from restaurants.serializers import RestaurantSerializer

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name']

class SubMenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubMenuCategory
        fields = ['name', 'cover_image']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class DishSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Dish
        fields = ['name', 'photo', 'ingredients']