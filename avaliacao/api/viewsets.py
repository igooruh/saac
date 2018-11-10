from rest_framework.viewsets import ModelViewSet
from avaliacao.models import Avaliacao
from .serializers import avaliacao_serializer


class avaliacao_viewSet(ModelViewSet):

    queryset = Avaliacao.objects.all()
    serializer_class = avaliacao_serializer