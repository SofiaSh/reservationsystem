from .models import Resourse
from rest_framework import serializers


class ResourseSerializer(serializers.HyperlinkedModelSerializer):
    """Класс для сериализации модели резервируевого объекта"""

    booking = serializers.HyperlinkedRelatedField(
        many=True, view_name='booking-detail', read_only=True)

    class Meta:
        model = Resourse
        fields = ('headline', 'description', 'id', 'booking')
