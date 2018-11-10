from rest_framework.serializers import  ModelSerializer
from comentario.models import Comentario

class comentario_serializar(ModelSerializer):

    class Meta:

        model = Comentario
        fields = '__all__'