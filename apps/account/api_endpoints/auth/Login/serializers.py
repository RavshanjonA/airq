from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from apps.account.models import Account
from rest_framework.fields import SerializerMethodField, CharField
from django.utils.translation import gettext_lazy as _


class LoginSerializer(ModelSerializer):
    email = CharField(max_length=100, required=True)
    password = CharField(max_length=68, write_only=True)
    tokens = SerializerMethodField(read_only=True)

    def get_tokens(self, obj):
        email = obj.get('email')
        tokens = Account.objects.get(email=email).tokens
        return tokens

    class Meta:
        model = Account
        fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)

        if not user:
            raise ValidationError(_("User not found."))
        if not user.is_active:
            raise ValidationError(_("User not active."))

        return {
            'email': user.email,
            'tokens': user.tokens  # This uses the get_tokens method above
        }
