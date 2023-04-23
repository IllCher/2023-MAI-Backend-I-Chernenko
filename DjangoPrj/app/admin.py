from app.models import Director, Film
from django.contrib import admin


class Admin(admin.ModelAdmin):
    list_display = ("id", "title", "year")


class DirectorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Film, Admin)
admin.site.register(Director, DirectorAdmin)
