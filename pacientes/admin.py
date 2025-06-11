from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_paciente', 'edad', 'genero', 'fecha_ingreso')
    search_fields = ('nombre_paciente', 'motivo_consulta')
    list_filter = ('genero', 'fecha_ingreso')

