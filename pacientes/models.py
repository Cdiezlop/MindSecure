from django.db import models

class Paciente(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    nombre_paciente = models.CharField(max_length=255)
    edad = models.IntegerField()
    genero = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    motivo_consulta = models.TextField()
    amnesis_psiquiatrica = models.TextField(blank=True, null=True)
    tratamiento = models.TextField(blank=True, null=True)
    plan_terapeutico = models.TextField(blank=True, null=True)
    fecha_ingreso = models.DateField()  # Si no usas hora, mejor mantenerlo simple
    eventos = models.JSONField(default=list, blank=True, null=True)

    def __str__(self):
        return self.nombre_paciente
