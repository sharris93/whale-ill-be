from django.urls import path
from .views import RegisterView

# /auth/...
urlpatterns = [
    path('register/', RegisterView.as_view())
]