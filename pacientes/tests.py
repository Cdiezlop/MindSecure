from django.test import TestCase
from .models import Paciente
from datetime import date

class PacienteModelTest(TestCase):
    def test_creacion_paciente(self):
        paciente = Paciente.objects.create(
            id='1000000000',
            nombre_paciente='Paciente de prueba',
            edad=30,
            genero='Masculino',
            fecha_nacimiento=date(1995, 6, 9),
            motivo_consulta='Evaluación inicial',
            fecha_ingreso=date.today()
        )
        self.assertEqual(paciente.nombre_paciente, 'Paciente de prueba')
