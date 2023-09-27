# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

from measurement.models import Measurement, Sensor
from measurement.serializers import SensorsSerializer, SensorDetailSerializer

class SensorsView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorsSerializer(sensors, many = True)
        return Response(ser.data)

    def post(self, request):
        name = request.data.get('name')
        description = request.data.get('description')
        Sensor(name = name, description = description ).save()
        return Response({'status': f'sensor {name} added'})
    
class MeasurementsView(APIView):
    
    def post(self, request):
        sensor = int(request.data.get('sensor'))
        temperature = request.data.get('temperature')
        Measurement(sensor_id = sensor, temperature = temperature).save()
        return Response({'status': 'temperature added'})
    
class SensorView(APIView):
    def get(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        ser = SensorDetailSerializer(sensor, many = True)
        return Response(ser.data)
    
    def patch(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        ser = SensorsSerializer(sensor, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
        return Response({'status': f'sensor update'})
