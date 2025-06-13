from django.db import models

class Medico(models.Model):
    id = models.CharField(primary_key=True, max_length=20)  # Documento de identidad
    nombre = models.CharField(max_length=40)
    puesto = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    clave_acceso = models.CharField(max_length=128)  # Almacenamiento encriptado

    def __str__(self):
        return self.nombre