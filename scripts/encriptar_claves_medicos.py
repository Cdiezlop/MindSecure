# scripts/encriptar_claves_medicos.py

import os
import django

# Configura el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mind_Secure.settings')
django.setup()

from django.contrib.auth.hashers import make_password
from medicos.models import Medico

def encriptar_claves():
    for medico in Medico.objects.all():
        if not medico.clave_acceso.startswith('pbkdf2_sha256$'):
            print(f"Cifrando clave de: {medico.nombre}")
            medico.clave_acceso = make_password(medico.clave_acceso)
            medico.save()

    print("Proceso de encriptación de claves finalizado.")

if __name__ == '__main__':
    encriptar_claves()