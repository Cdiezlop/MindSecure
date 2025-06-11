# MindSecure – Parte Base de Datos

## Rol: Cristian David Diez López

Responsabilidades cumplidas:

- Definición de modelos para Medico y Paciente.
- Serialización para consumo desde la API REST.
- Registro en Django Admin.
- Carga de datos iniciales (fixtures) para pruebas.
- Estructura lista para integración backend.

## Para cargar los datos de prueba hacer lo sigiente: 

```bash
python manage.py loaddata medicos/fixtures/medicos_fixture.json
python manage.py loaddata pacientes/fixtures/pacientes_fixture.json
