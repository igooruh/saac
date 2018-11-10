from rest_framework.viewsets import ModelViewSet
from medico.models import Medico
from .serializers import medico_serializer

class medico_viewSet(ModelViewSet):

    queryset = Medico.objects.all()
    serializer_class = medico_serializer