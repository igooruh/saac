from rest_framework.serializers import ModelSerializer
from core_consultas.models import Consultas

class consultas_Serializer(ModelSerializer):

    class Meta:

        model = Consultas
        fields = ('id', 'nome', 'descricao')