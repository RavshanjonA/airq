from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.monitoring.api_endpoints.current.serializers import SummarySerializer
from apps.monitoring.api_endpoints.history.serializers import HistorySerializer
from apps.monitoring.api_endpoints.history.services import history_statistics


class HistoryView(GenericAPIView):
    """
        Handles requests for historical environmental data and statistics based on geolocation.

        This view processes data submitted via POST request, validates the input using `HistorySerializer`,
        computes statistics using the `historical_statistics` function, and returns a summarized response
        serialized with `SummarySerializer`.

        ## Attributes:
            serializer_class (HistorySerializer): Serializer for validating and deserializing input data.

        ## HTTP Methods:
            POST:
                Purpose:
                    - Accepts latitude , longitude, start, end, as input.
                    - Computes and returns environmental statistics based on the provided geolocation.

                Request Body:
                    {
                        "latitude": float,
                        "longitude": float,
                        "start": int,
                        "end": int
                    }

                Request Body Serializer:
                    - `HistorySerializer`

                Response:
                    - HTTP 200 OK:
                        Serialized response using `SummarySerializer`.
                        Example:
                        {
                            "coord": {
                                "lat": 40,
                                "lon": 74
                            },
                            "list": [
                                {
                                    "dt": 1605182400,
                                    "main": {
                                        "aqi": 2
                                    },
                                    "components": {
                                        "co": 201.94,
                                        "no": 0.12,
                                        "no2": 0.13,
                                        "o3": 68.35,
                                        "so2": 0.6,
                                        "pm2_5": 8.03,
                                        "pm10": 8.03,
                                        "nh3": 0.06
                                    }
                                }{
                                    "dt": 1605192400,
                                    "main": {
                                        "aqi": 2
                                    },
                                    "components": {
                                        "co": 201.94,
                                        "no": 0.12,
                                        "no2": 0.13,
                                        "o3": 68.35,
                                        "so2": 0.6,
                                        "pm2_5": 8.03,
                                        "pm10": 8.03,
                                        "nh3": 0.06
                                    }
                                }
                            ]
                        }

                Example Input:
                    POST /history
                    {
                        "latitude": 40.7128,
                        "longitude": 40.7128,
                        "start": 1605182400,
                        "end": 1605192400
                    }

                Validation:
                    - Ensures the latitude, longitude, start and end fields are provided and correctly formatted.
                    - Validates the existence of the `id` field if required.

                Processing:
                    - Validates the input data using `HistorySerializer`.
                    - Computes statistics using the `historical_statistics` function.
                    - Serializes computed data with `SummarySerializer`.

                Usage:
                    - Ideal for applications requiring historical environmental data and analysis
                      based on user-specified geolocation.

                Notes:
                    - This endpoint assumes that the `historical_statistics` function is implemented
                      and returns data compatible with the structure defined in `SummarySerializer`.
    """
    serializer_class = HistorySerializer

    @swagger_auto_schema(
        request_body=HistorySerializer,
        responses={
            status.HTTP_200_OK: SummarySerializer(),
        }
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        statistics = history_statistics(**data)
        serializer.save()
        serializer = SummarySerializer(data=statistics)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.validated_data, status=status.HTTP_200_OK)


__all__ = ("HistoryView",)
