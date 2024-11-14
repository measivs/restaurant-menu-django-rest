from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from .filters import SubMenuCategoryFilter
from .models import MenuCategory, SubMenuCategory, Dish, Ingredient
from .serializers import MenuCategorySerializer, SubMenuCategorySerializer, DishSerializer, IngredientSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        restaurant = self.request.user.restaurants.first()
        if not restaurant:
            raise ValidationError({"error": "User must be associated with a restaurant"})
        serializer.save(restaurant=restaurant)

    def perform_update(self, serializer):
        restaurant = self.request.user.restaurants.first()
        if not restaurant:
            raise ValidationError({"error": "User must be associated with a restaurant"})
        serializer.save(restaurant=restaurant)


class SubMenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubMenuCategory.objects.all()
    serializer_class = SubMenuCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        restaurant = self.request.user.restaurants.first()
        if not restaurant:
            raise ValidationError({"error": "User must be associated with a restaurant"})
        serializer.save(restaurant=restaurant)

    def perform_update(self, serializer):
        restaurant = self.request.user.restaurants.first()
        if not restaurant:
            raise ValidationError({"error": "User must be associated with a restaurant"})
        serializer.save(restaurant=restaurant)


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        restaurant = self.request.user.restaurants.first()
        if not restaurant:
            raise ValidationError({"error": "User must be associated with a restaurant"})
        dish = serializer.save(restaurant=restaurant)
        ingredients_data = self.request.data.get('ingredients', [])
        if ingredients_data:
            for ingredient_data in ingredients_data:
                Ingredient.objects.create(dish=dish, **ingredient_data)

    def perform_update(self, serializer):
        restaurant = self.request.user.restaurants.first()
        if not restaurant:
            raise ValidationError({"error": "User must be associated with a restaurant"})
        dish = serializer.save(restaurant=restaurant)
        ingredients_data = self.request.data.get('ingredients', [])
        if ingredients_data:
            dish.ingredients.all().delete()
            for ingredient_data in ingredients_data:
                Ingredient.objects.create(dish=dish, **ingredient_data)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]