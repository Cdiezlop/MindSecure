from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Medico

class MedicoSerializer(serializers.ModelSerializer):
    clave_acceso = serializers.CharField(write_only=True)  

    class Meta:
        model = Medico
        fields = ['id', 'nombre', 'puesto', 'email', 'clave_acceso']

    def validate_clave_acceso(self, value):
        """Encripta la contraseña antes de guardarla"""
        return make_password(value)

    def create(self, validated_data):
        """Crea un médico con la contraseña encriptada"""
        validated_data['clave_acceso'] = make_password(validated_data['clave_acceso'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """Actualiza la contraseña si se proporciona"""
        if 'clave_acceso' in validated_data:
            validated_data['clave_acceso'] = make_password(validated_data['clave_acceso'])
        return super().update(instance, validated_data)