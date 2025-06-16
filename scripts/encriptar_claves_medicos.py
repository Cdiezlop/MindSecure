import os
import django

# Configura el entorno Django
# Asegúrate de que 'Mind_Secure.settings' apunte a tu archivo settings.py principal
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mind_Secure.settings')
django.setup()

from django.contrib.auth.hashers import make_password
from medicos.models import Medico

def encriptar_claves():
    """
    Encripta las claves de acceso de los médicos que aún no han sido cifradas.
    Verifica si la clave ya está en formato hash para evitar doble cifrado.
    """
    print("Iniciando proceso de encriptación de claves de médicos...")
    medicos_actualizados = 0
    for medico in Medico.objects.all():
        # Django utiliza 'pbkdf2_sha256$' como prefijo para las claves hasheadas por defecto
        if not medico.clave_acceso.startswith('pbkdf2_sha256$'):
            print(f"Cifrando clave para el médico: {medico.nombre} (ID: {medico.id})")
            medico.clave_acceso = make_password(medico.clave_acceso)
            medico.save()
            medicos_actualizados += 1
        else:
            print(f"La clave del médico: {medico.nombre} (ID: {medico.id}) ya está cifrada. Omitiendo.")

    print(f"Proceso de encriptación de claves finalizado. Claves actualizadas: {medicos_actualizados}.")

if __name__ == '__main__':
    encriptar_claves()
