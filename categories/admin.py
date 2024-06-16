from django.contrib import admin
from categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  
    class Meta:
        list_display = ('__all__',)
        search_fields = ('__all__',)


