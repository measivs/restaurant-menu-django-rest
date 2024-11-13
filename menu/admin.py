from django.contrib import admin
from .models import MenuCategory, SubMenuCategory, Dish, Ingredient

admin.site.register(MenuCategory)
admin.site.register(SubMenuCategory)
admin.site.register(Dish)
admin.site.register(Ingredient)
