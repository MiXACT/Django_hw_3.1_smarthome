# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from measurement.models import Sensor
from measurement.serializers import SensorSerializer


# @api_view(['GET'])
# def sensors(request):
#     sens = Sensor.objects.all()
#     ser = SensorSerializer(sens, many=True)
#     return Response(ser.data)


class SensGetPost(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensModify(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
