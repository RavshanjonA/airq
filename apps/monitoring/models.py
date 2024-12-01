from django.db.models import CharField

from apps.shared.models import TimeStampedModel


class Current(TimeStampedModel):
    latitude = CharField(max_length=255)
    longitude = CharField(max_length=255)
