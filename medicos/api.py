from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password
from .serializers import MedicoSerializer
from django.shortcuts import redirect
from .models import Medico
from .serializers import CambioClaveSerializer

class EditarPerfilAPIView(APIView):
    def post(self, request):
        medico_id = request.data.get('id')
        nuevo_nombre = request.data.get('nombre')
        nuevo_email = request.data.get('email')

        if not all([medico_id, nuevo_nombre, nuevo_email]):
            return Response({'error': 'Todos los campos son obligatorios.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            medico = Medico.objects.get(id=medico_id)
        except Medico.DoesNotExist:
            return Response({'error': 'Médico no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        # Verificar si el nuevo email ya está en uso por otro médico
        if Medico.objects.filter(email=nuevo_email).exclude(id=medico_id).exists():
            return Response({'error': 'El email ya está en uso por otro médico.'}, status=status.HTTP_400_BAD_REQUEST)

        medico.nombre = nuevo_nombre
        medico.email = nuevo_email
        medico.save()

        return Response({'mensaje': 'Perfil actualizado exitosamente.'}, status=status.HTTP_200_OK)

class CambiarClaveAPIView(APIView):
    print("al fin, dios es grnade")
    def post(self, request):
        medico_id = request.data.get('id')
        clave_actual = request.data.get('clave_actual')
        nueva_clave = request.data.get('nueva_clave')
        confirmar_clave = request.data.get('confirmar_clave')

        if not all([medico_id, clave_actual, nueva_clave, confirmar_clave]):
            return Response({'error': 'Todos los campos son obligatorios.'}, status=status.HTTP_400_BAD_REQUEST)

        if nueva_clave != confirmar_clave:
            return Response({'error': 'Las nuevas contraseñas no coinciden.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            medico = Medico.objects.get(id=medico_id)
        except Medico.DoesNotExist:
            return Response({'error': 'Médico no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        if not check_password(clave_actual, medico.clave_acceso):
            return Response({'error': 'La contraseña actual es incorrecta.'}, status=status.HTTP_401_UNAUTHORIZED)

        medico.clave_acceso = make_password(nueva_clave)
        medico.save()

        return Response({'mensaje': 'Contraseña actualizada exitosamente.'}, status=status.HTTP_200_OK)
    
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
                    'puesto': medico.puesto,
                    'email': medico.email
                }
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Clave de acceso incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)
