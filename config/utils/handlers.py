from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, ValidationError):
            # Handle validation errors to return in the desired format
            errors = []
            for field, messages in exc.detail.items():
                for message in messages:
                    errors.append({
                        "code": message.code if hasattr(message, 'code') else "error",
                        "detail": str(message),
                        "attr": field
                    })
            response.data = {
                "type": "validation_error",
                "errors": errors
            }
        else:
            # Standardized error response format for other exceptions
            response.data = {
                "success": False,
                "error": {
                    "type": exc.__class__.__name__,
                    "message": response.data.get("detail", str(exc)),
                    "code": response.status_code,
                }
            }
    else:
        # Handle non-DRF exceptions
        response = Response(
            {
                "success": False,
                "error": {
                    "type": "ServerError",
                    "message": "An unexpected error occurred.",
                    "code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                },
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return response
