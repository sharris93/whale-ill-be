from django.urls import path
from .views import RegisterView, LoginView

# /auth/...
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view())
]