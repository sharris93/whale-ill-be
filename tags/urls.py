from django.urls import path
from .views import TagListView, TagDetailView

# /tags/
urlpatterns = [
    path('', TagListView.as_view()),
    path('<int:pk>/', TagDetailView.as_view())
]