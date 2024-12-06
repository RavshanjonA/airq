from rest_framework.serializers import ModelSerializer

from apps.monitoring.models import History


class HistorySerializer(ModelSerializer):
    class Meta:
        model = History
        fields = ("id", "start", "end", "latitude", "longitude")
