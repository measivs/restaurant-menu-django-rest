from rest_framework import viewsets
from .models import MenuCategory, SubMenuCategory, Dish, Ingredient
from .serializers import MenuCategorySerializer, SubMenuCategorySerializer, DishSerializer, IngredientSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SubMenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubMenuCategory.objects.all()
    serializer_class = SubMenuCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        restaurant = self.request.user.restaurants.first()
        serializer.save(restaurant=restaurant)

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]