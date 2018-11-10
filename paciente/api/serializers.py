from rest_framework.serializers import ModelSerializer
from paciente.models import Paciente

class paciente_serializer(ModelSerializer):

    class Meta:

        model = Paciente
        fields = '__all__'