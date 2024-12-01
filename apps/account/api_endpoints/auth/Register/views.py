from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from apps.account.api_endpoints.auth.Register.serializers import RegisterSerializer  # noqa E501
from apps.account.models import Account


class RegisterView(CreateAPIView):
    """
        View for user registration.

        This view handles user registration by accepting user input for email, password, and password confirmation.
        It uses the `RegisterSerializer` to validate the data, check for duplicate emails, and create a new user account.
        The account will be created with an inactive status, and the password will be hashed and stored securely.

        ## Methods:
            post(request):
                Handles the HTTP POST request for user registration.
                Accepts the user's email, password, and password confirmation,
                validates the input data, and creates the user account.
                Returns a response indicating success or failure.

        ## Response:
            - On success (HTTP 201 Created), returns the newly created user account's details (email).
            - On failure (HTTP 400 Bad Request), returns validation errors.
    """
    queryset = Account.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        tags=["auth"],
        request_body=RegisterSerializer,
        responses={
            status.HTTP_201_CREATED: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "email": openapi.Schema(type=openapi.TYPE_STRING, description="User email"),
                    "id": openapi.Schema(type=openapi.TYPE_INTEGER, description="User id"),
                },
                example={
                    "email": "user@example.com",
                    "id": "1",
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
                            "code": "unique",
                            "detail": "Account with this email already exists.",
                            "attr": "email",
                        }
                    ],
                },
            ),
        },
        examples={
            "application/json": {
                "email": "user@example.com",
                "password": "password123",
                "password2": "password123",
            },
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


__all__ = [
    "RegisterView",
]
