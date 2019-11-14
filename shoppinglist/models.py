from django.db import models

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100)
    shop_site = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name