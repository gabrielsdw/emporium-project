from django.contrib import admin
from brands.models import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name',)

