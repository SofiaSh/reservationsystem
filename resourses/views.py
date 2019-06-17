from rest_framework import permissions, viewsets
from .models import Resourse
from booking.permissions import IsOwnerOrReadOnly
from .serializers import ResourseSerializer


class ResouserViewSet(viewsets.ModelViewSet):
    """Класс позволяет автоматически выполнять действия методов list, create,
    update и destroy"""
    queryset = Resourse.objects.all()
    serializer_class = ResourseSerializer




