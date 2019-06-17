from .models import Resourse
from rest_framework import serializers
from booking.serializers import BookingSerializer


class ResourseSerializer(serializers.HyperlinkedModelSerializer):
    """Класс для сериализации модели резервируевого объекта"""

    booking = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = Resourse
        fields = ('headline', 'description', 'id', 'booking')
