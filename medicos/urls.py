from django.urls import path
from .api import CambiarClaveAPIView, EditarPerfilAPIView


urlpatterns = [
    path('api/editar-perfil-medico/', EditarPerfilAPIView.as_view(), name='editar-perfil-medico'),
    path('api/cambiar-clave-medico/', CambiarClaveAPIView.as_view(), name='cambiar-clave-medico'),
]
