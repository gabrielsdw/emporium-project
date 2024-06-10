from django.db import models
from brands.models import Brand
from categories.models import Category
from colors.models import Color



class Product(models.Model):
    name = models.CharField(max_length=100)
    is_avaible = models.BooleanField()
    avaible_colors = models.ManyToManyField(Color, related_name='products')
    main_photo = models.ImageField(upload_to='products/')
    selling_price = models.DecimalField(max_digits=20, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    description = models.TextField(null=True, blank=True)


    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name
    