from rest_framework.viewsets import ModelViewSet
from comentario.models import Comentario
from .serializers import comentario_serializar

class comentario_viewSet(ModelViewSet):

    queryset = Comentario.objects.all()
    serializer_class = comentario_serializar