from rest_framework import serializers
from .models import Paciente
from rest_framework.reverse import reverse

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'  # o especifica los campos manualmente si prefieres

class PacienteListSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Paciente
        fields = ['id', 'nombre_paciente', 'url']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse('paciente-detalles-detail', kwargs={'pk': obj.pk}, request=request)
