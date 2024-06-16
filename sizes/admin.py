from django.contrib import admin
from . import models


@admin.register(models.Size)
class SizeAdmin(admin.ModelAdmin):
    
    class Meta:
        list_display = ('__all__',)
        search_fields = ('__all__',)
