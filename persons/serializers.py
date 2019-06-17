from .models import Person
from booking.serializers import BookingSerializer
from rest_framework import serializers


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    """Класс для сериализации модели персоны"""
    #booking = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = ('username', 'email', 'first_name', 'patronymic', 'last_name',
                  'is_staff', 'biography', 'booking')
