from rest_framework import routers
from .api import PacienteViewVet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PacienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

