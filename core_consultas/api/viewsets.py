from rest_framework.viewsets import ModelViewSet
from core_consultas.models import Consultas
from .serializers import consultas_Serializer

class SaacViewSet(ModelViewSet):

    queryset = Consultas.objects.all()
    serializer_class = consultas_Serializer