from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
      
      class Meta:
        list_display = ('__all__',)
        search_fields = ('__all__',)

