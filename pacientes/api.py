from rest_framework import viewsets, mixins, permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import action
from .models import Paciente
from .serializers import PacienteSerializer, PacienteListSerializer


class PacienteListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteListSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        pacientes = self.get_queryset()
        serializer = self.get_serializer(pacientes, many=True, context={'request': request})
        
        crear_url = request.build_absolute_uri('/pacientes/api/pacientes/nuevo/')
        buscar_url = request.build_absolute_uri('/pacientes/api/pacientes/lista/buscar/')
        cambiar_clave_url = request.build_absolute_uri(reverse('cambiar-clave-medico'))
        editar_perfil_url = request.build_absolute_uri(reverse('editar-perfil-medico'))

        return Response({
            'editar_perfil_url': editar_perfil_url,
            'crear_paciente_url': crear_url,
            'buscar_paciente_url': buscar_url,
            'cambiar_clave_url': cambiar_clave_url,
            'pacientes': serializer.data
        })

    @action(detail=False, methods=['get'], url_path='buscar')
    def buscar_por_nombre(self, request):
        nombre = request.query_params.get('nombre', '')
        pacientes = Paciente.objects.filter(nombre_paciente__icontains=nombre)
        serializer = self.get_serializer(pacientes, many=True, context={'request': request})

        crear_url = request.build_absolute_uri('/pacientes/api/pacientes/nuevo/')
        buscar_url = request.build_absolute_uri('/pacientes/api/pacientes/lista/buscar/')
        cambiar_clave_url = request.build_absolute_uri(reverse('cambiar-clave-medico'))
        
        return Response({
            'crear_paciente_url': crear_url,
            'buscar_paciente_url': buscar_url,
            'cambiar_clave_url': cambiar_clave_url,
            'pacientes_filtrados': serializer.data
        })


class PacienteCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [permissions.AllowAny]
    
class PacienteDetailViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,  viewsets.GenericViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [permissions.AllowAny] 
    
