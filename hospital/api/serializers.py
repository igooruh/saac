from rest_framework.serializers import ModelSerializer
from hospital.models import Hospital

class hopital_serializer(ModelSerializer):

    class Meta:

        model = Hospital
        fields = '__all__'