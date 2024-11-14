from django.db import models
from mptt.models import MPTTModel
from restaurants.models import Restaurant

# Create your models here.

class MenuCategory(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_categories', default=1)

    class Meta:
        verbose_name_plural = 'MenuCategories'

    def __str__(self):
        return self.name


class SubMenuCategory(models.Model):
    name = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='submenu_categories/', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True)
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        verbose_name_plural = 'SubMenuCategories'

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='dishes/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    submenu_category = models.ForeignKey(SubMenuCategory, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Dishes'


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return self.name

