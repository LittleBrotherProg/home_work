from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length = 100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name = 'measurements')
    temperature = models.FloatField()
    time = models.DateTimeField(auto_now=True) 

