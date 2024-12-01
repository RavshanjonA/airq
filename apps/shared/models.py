from django.db.models import DateTimeField, Model, SlugField

from django.utils.translation import gettext_lazy as _


class TimeStampedModel(Model):
    created_at = DateTimeField(verbose_name=_("Created At"), auto_now_add=True)
    updated_at = DateTimeField(verbose_name=_("Updated At"), auto_now=True)

    class Meta:
        abstract = True


class SlugStampedModel(TimeStampedModel):
    slug = SlugField(verbose_name=_("Slug"), unique=True)

    class Meta:
        abstract = True
