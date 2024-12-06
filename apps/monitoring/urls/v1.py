from django.urls import path
from apps.monitoring.api_endpoints import current, history

urlpatterns = [
    path('current/', current.CurrentView.as_view(), name="current"),
    path('history/', history.HistoryView.as_view(), name="history"),
]
