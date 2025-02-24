from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Tag
from .serializers.common import TagSerializer


# ListCreate view / index & create
class TagListView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# RetrieveUpdateDestroy view / show, update & delete
class TagDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer