from rest_framework.fields import IntegerField, FloatField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.monitoring.models import Current


# for request
class CurrentSerializer(ModelSerializer):
    class Meta:
        model = Current
        fields = ("id", "latitude", "longitude")


# for response
class CoordSerializer(Serializer):
    lat = IntegerField()
    lon = IntegerField()


class AqiSerializer(Serializer):
    aqi = IntegerField()


class ComponentSerializer(Serializer):
    co = FloatField()
    no = FloatField()
    no2 = FloatField()
    o3 = FloatField()
    so2 = FloatField()
    pm2_5 = FloatField()
    pm10 = FloatField
    nh3 = FloatField()


class ListSerializer(Serializer):
    dt = IntegerField()
    main = AqiSerializer()
    components = ComponentSerializer()


class SummarySerializer(Serializer):
    coord = CoordSerializer()
    list = ListSerializer(many=True)
