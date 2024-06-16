from django.contrib import admin
from brands.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
   
    class Meta:
        list_display = ('__all__',)
        search_fields = ('__all__',)


