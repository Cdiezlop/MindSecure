from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import Medico

class MedicoSerializer(serializers.ModelSerializer):
    clave_acceso = serializers.CharField(write_only=True)  

    class Meta:
        model = Medico
        fields = ['id', 'nombre', 'puesto', 'email', 'clave_acceso']

    def create(self, validated_data):
        validated_data['clave_acceso'] = make_password(validated_data['clave_acceso'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'clave_acceso' in validated_data:
            validated_data['clave_acceso'] = make_password(validated_data['clave_acceso'])
        return super().update(instance, validated_data)
    
class CambioClaveSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    clave_actual = serializers.CharField(write_only=True)
    nueva_clave = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            medico = Medico.objects.get(id=data['id'])
        except Medico.DoesNotExist:
            raise serializers.ValidationError("Médico no encontrado.")

        if not check_password(data['clave_actual'], medico.clave_acceso):
            raise serializers.ValidationError("La clave actual es incorrecta.")

        return data

    def save(self):
        medico = Medico.objects.get(id=self.validated_data['id'])
        medico.clave_acceso = make_password(self.validated_data['nueva_clave'])
        medico.save()
        return medico
