"""saac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from core_consultas.api.viewsets import Saac_viewSet
from avaliacao.api.viewsets import avaliacao_viewSet
from comentario.api.viewsets import comentario_viewSet
from hospital.api.viewsets import hospital_viewSet
from medico.api.viewsets import medico_viewSet
from paciente.api.viewsets import paciente_viewSet

router = routers.DefaultRouter()
router.register(r'saac/consultas', Saac_viewSet)
router.register(r'saac/avaliacao', avaliacao_viewSet)
router.register(r'saac/comentario', comentario_viewSet)
router.register(r'saac/hospital', hospital_viewSet)
router.register(r'saac/medico', medico_viewSet)
router.register(r'saac/paciente', paciente_viewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
