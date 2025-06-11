from .models import Paciente
from rest_framework import viewsets, permissions
from .serializers import PacienteSerializer

class PacienteViewVet(viewsets.ModelViewSet):
    queryset= Paciente.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class= PacienteSerializer