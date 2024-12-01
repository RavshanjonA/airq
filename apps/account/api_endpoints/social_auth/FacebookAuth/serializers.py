from rest_framework import serializers

from ..register import register_social_user
from .facebook_auth import Facebook


class FacebookSocialAuthSerializer(serializers.Serializer):
    """Handles serialization of facebook related data"""

    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = Facebook.validate(auth_token)

        try:
            user_id = user_data["id"]
            email = user_data["email"]
            name = user_data["name"]
            provider = "facebook"
            return register_social_user(
                provider=provider, user_id=user_id, email=email, name=name
            )
        except Exception:

            raise serializers.ValidationError(
                "The token  is invalid or expired. Please login again."
            )
