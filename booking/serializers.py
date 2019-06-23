from .models import Booking
from resourses.models import Resourse
from rest_framework import serializers


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    """Класс для сериализации модели бронирования"""

    owner = serializers.ReadOnlyField(source='owner.username')
    resourse = serializers.PrimaryKeyRelatedField(queryset=Resourse.objects.all())

    class Meta:
        model = Booking
        fields = ('owner', 'resourse', 'start_time', 'end_time')
