from rest_framework.viewsets import ModelViewSet
from hospital.models import Hospital
from .serializers import hopital_serializer

class hospital_viewSet(ModelViewSet):

    queryset = Hospital.objects.all()
    serializer_class = hopital_serializer