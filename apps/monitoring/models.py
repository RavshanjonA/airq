from django.db.models import CharField, FloatField

from apps.shared.models import TimeStampedModel


class Current(TimeStampedModel):
    latitude = CharField(max_length=255)
    longitude = CharField(max_length=255)


class History(TimeStampedModel):
    start = CharField(max_length=255)
    end = CharField(max_length=255)
    latitude = FloatField()
    longitude = FloatField()
