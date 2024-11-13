from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)
    cover_image = models.ImageField(upload_to='restaurant_covers/', blank=True, null=True)

    def __str__(self):
        return self.name

