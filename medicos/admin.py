from django.contrib import admin
from .models import Medico

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'puesto')
    search_fields = ('nombre', 'puesto')
