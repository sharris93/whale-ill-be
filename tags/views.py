from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Tag
from .serializers.common import TagSerializer
from rest_framework.permissions import IsAdminUser


# ListCreate view / index & create
class TagListView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# RetrieveUpdateDestroy view / show, update & delete
class TagDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer