from .models import Person
from rest_framework import serializers


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    """Класс для сериализации модели персоны"""
    booking = serializers.HyperlinkedRelatedField(
        many=True, view_name='booking-detail', read_only=True)

    class Meta:
        model = Person
        fields = ('username', 'email', 'first_name', 'patronymic', 'last_name',
                  'is_staff', 'biography', 'booking')
