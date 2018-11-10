from rest_framework.serializers import ModelSerializer
from avaliacao.models import Avaliacao

class avaliacao_serializer(ModelSerializer):

    class Meta:

        model = Avaliacao
        fields = '__all__'