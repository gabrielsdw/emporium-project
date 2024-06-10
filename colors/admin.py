from django.contrib import admin
from colors.models import Color


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name',)

