from rest_framework.viewsets import ModelViewSet
from paciente.models import Paciente
from .serializers import paciente_serializer

class paciente_viewSet(ModelViewSet):

    queryset = Paciente.objects.all()
    serializer_class = paciente_serializer