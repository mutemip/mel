from django.contrib import admin

from .models import HomeApp

class homeAppAdmin(admin.ModelAdmin):
    list_display = ('home', 'age', 'salary')

admin.site.register(HomeApp, homeAppAdmin)
