from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .serializers import MedicoSerializer
from django.shortcuts import redirect
from .models import Medico
from .serializers import CambioClaveSerializer

class CambiarClaveAPIView(APIView):
    def post(self, request):
        serializer = CambioClaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Contraseña cambiada exitosamente'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MedicoViewVet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedicoSerializer

class LoginMedicoAPIView(APIView):
    def post(self, request):
        medico_id = request.data.get('id')
        clave_acceso = request.data.get('clave_acceso')

        if not medico_id or not clave_acceso:
            return Response({'error': 'ID y clave_acceso son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            medico = Medico.objects.get(id=medico_id)
        except Medico.DoesNotExist:
            return Response({'error': 'Médico no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        if check_password(clave_acceso, medico.clave_acceso):
            return Response({
                'mensaje': 'Login exitoso',
                'redirect_to': 'http://127.0.0.1:8000/pacientes/api/pacientes/lista',
                'medico': {
                    'id': medico.id,
                    'nombre': medico.nombre,
                    'puesto': medico.puesto
                }
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Clave de acceso incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)
