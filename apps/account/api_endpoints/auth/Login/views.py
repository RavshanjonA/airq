from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.account.api_endpoints.auth.Login.serializers import LoginSerializer


class LoginView(TokenObtainPairView):
    """
    Login View

    This view provides an API endpoint for user authentication. It utilizes the
   `TokenObtainPairView` to issue access and refresh tokens upon successful login.

   **Features**:
   - **Login**: Authenticates a user based on provided credentials and returns JWT tokens.
   - **Token Generation**: Issues an access token and a refresh token for the authenticated user.


   **Attributes**:
       permission_classes (tuple): Allows unrestricted access to this endpoint by
           setting `AllowAny` permission.
       serializer_class (Serializer): The serializer used to handle input data
           validation and token generation, implemented in `LoginSerializer`.


   """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        tags=["auth"],
        request_body=LoginSerializer,
        responses={
            status.HTTP_200_OK: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "email": openapi.Schema(type=openapi.TYPE_STRING, description="User email"),
                    "tokens": openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "access": openapi.Schema(type=openapi.TYPE_STRING, description="Access token"),
                            "account_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="Account ID"),
                            "expires_in": openapi.Schema(type=openapi.TYPE_STRING, description="Expire Datetime"),
                            "refresh": openapi.Schema(type=openapi.TYPE_STRING, description="Refresh token"),
                        },
                    ),
                },
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "type": openapi.Schema(type=openapi.TYPE_STRING,
                                           description="Type of the error, e.g., 'validation_error'"),
                    "errors": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "code": openapi.Schema(type=openapi.TYPE_STRING, description="Error code"),
                                "detail": openapi.Schema(type=openapi.TYPE_STRING,
                                                         description="Detailed error message"),
                                "attr": openapi.Schema(type=openapi.TYPE_STRING,
                                                       description="Attribute causing the error"),
                            },
                        ),
                    ),
                },
                example={
                    "type": "validation_error",
                    "errors": [
                        {
                            "code": "invalid",
                            "detail": "User not found.",
                            "attr": "non_field_error",
                        }
                    ],
                },
            ),
        },
        examples={
            "application/json": {
                "email": "user@example.com",
                "password": "password123",
            },
        },
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.data.get('tokens')
        return Response(tokens)


__all__ = ("LoginView",)
