from rest_framework import routers
from .api import MedicoViewVet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicoViewSet

router = DefaultRouter()
router.register(r'', MedicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

