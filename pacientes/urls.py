from rest_framework import routers
from .api import PacienteListViewSet, PacienteCreateViewSet, PacienteDetailViewSet


router = routers.DefaultRouter()

router.register(r'api/pacientes/lista', PacienteListViewSet, basename='paciente-lista')
router.register(r'api/pacientes/nuevo', PacienteCreateViewSet, basename='paciente-nuevo')
router.register(r'api/pacientes/detalles', PacienteDetailViewSet, basename='paciente-detalles')
urlpatterns = router.urls