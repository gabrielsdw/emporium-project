from django.contrib import admin
from . import models


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    class Meta:
        list_display = ('__all__',)
        search_fields = ('__all__',)
