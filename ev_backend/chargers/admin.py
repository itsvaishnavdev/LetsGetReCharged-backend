from django.contrib import admin
from .models import EVCharger

@admin.register(EVCharger)
class EVChargerAdmin(admin.ModelAdmin):
    list_display = ('name', 'charger_type', 'power_kw', 'is_available', 'is_active')
    list_filter = ('charger_type', 'is_available')
    search_fields = ('name',)
