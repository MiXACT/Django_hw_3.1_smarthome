# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from measurement.models import Sensor
from measurement.serializers import SensorSerializer


@api_view(['GET'])
def sensors(request):
    sens = Sensor.objects.all()
    ser = SensorSerializer(sens, many=True)
    return Response(ser.data)
