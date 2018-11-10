from rest_framework.serializers import ModelSerializer
from medico.models import Medico

class medico_serializer(ModelSerializer):

    class Meta:

        model = Medico
        fields = '__all__'