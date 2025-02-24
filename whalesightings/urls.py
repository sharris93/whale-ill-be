from django.urls import path
from .views import WhaleSightingListView

# /whalesightings/
urlpatterns = [
    path('', WhaleSightingListView.as_view())
]