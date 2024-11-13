from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuCategoryViewSet, SubMenuCategoryViewSet, DishViewSet, IngredientViewSet

router = DefaultRouter()
router.register(r'menu_categories', MenuCategoryViewSet)
router.register(r'submenu_categories', SubMenuCategoryViewSet)
router.register(r'dishes', DishViewSet)
router.register(r'ingredients', IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
