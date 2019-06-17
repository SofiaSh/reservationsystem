from rest_framework import permissions, viewsets
from .models import Booking
from booking.permissions import IsOwnerOrReadOnly
from .serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """Класс позволяет автоматически выполнять действия методов list, create,
    update и destroy"""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
