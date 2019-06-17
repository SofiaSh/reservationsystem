from .serializers import PersonSerializer
from .models import Person
from rest_framework import viewsets


class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    """Класс позволяет автоматически выполнять retrieve и list"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
