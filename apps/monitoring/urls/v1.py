from django.urls import path
from apps.monitoring.api_endpoints import current

urlpatterns = [
    path('current/', current.CurrentView.as_view(), name="current")
]
