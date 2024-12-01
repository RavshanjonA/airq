from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.account.api_endpoints.social_auth.GoogleAuth.serializers import (
    GoogleSocialAuthSerializer,
)


class GoogleSocialAuthView(GenericAPIView):
    serializer_class = GoogleSocialAuthSerializer

    @swagger_auto_schema(
        tags=[
            "social-auth",
        ]
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = (serializer.validated_data)["auth_token"]
        return Response(data, status=status.HTTP_200_OK)


__all__ = ("GoogleSocialAuthView",)
