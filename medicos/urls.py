from rest_framework import routers
from django.urls import path
from .api import MedicoViewVet, CambiarClaveAPIView

router = routers.DefaultRouter()
router.register('api/medicos', MedicoViewVet, 'medicos')

urlpatterns = router.urls + [
    path('api/medicos/cambiar-clave/', CambiarClaveAPIView.as_view(), name='cambiar-clave-medico'),
]