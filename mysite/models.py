from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    image = models.CharField(max_length=500, default="https://p.kindpng.com/picc/s/79-798754_hoteles-y-centros-vacacionales-dish-placeholder-hd-png.png")

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('mysite:detailview', kwargs={'pk': self.pk})