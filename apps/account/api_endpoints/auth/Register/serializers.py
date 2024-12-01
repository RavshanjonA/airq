from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.account.models import Account
from django.utils.translation import gettext_lazy as _


class RegisterSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True)
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "password",
            "password2",
        )

    def validate_email(self, value):
        if Account.objects.filter(email=value).exists():
            raise ValidationError(_("Account already exists."))
        return value

    def create(self, validated_data):
        account = Account.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )
        account.set_password(validated_data["password"])
        account.save()
        return account
