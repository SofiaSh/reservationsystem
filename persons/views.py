from .serializers import PersonSerializer
from .models import Person
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    """Класс позволяет автоматически выполнять retrieve и list"""
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'

    def get(self, request):
        queryset = Person.objects.all()
        return Response({'persons': queryset})
