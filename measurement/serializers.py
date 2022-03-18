from rest_framework import serializers
from measurement.models import Sensor

# TODO: опишите необходимые сериализаторы


class SensorSerializer(serializers.ModelSerializer):
    # name = serializers.CharField()
    # description = serializers.CharField()
    class Meta:
        model = Sensor
        fields = '__all__'
