from django.test import TestCase
from .models import Medico

class MedicoModelTest(TestCase):
    def test_creacion_medico(self):
        medico = Medico.objects.create(
            id='9999999999',
            nombre='Test Doctor',
            puesto='Psiquiatra',
            email='test@hospital.com',
            clave_acceso='clave123'
        )
        self.assertEqual(medico.nombre, 'Test Doctor')

