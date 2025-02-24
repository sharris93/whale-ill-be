from rest_framework.views import APIView
from rest_framework.response import Response
from .models import WhaleSighting

# Serializers
from .serializers.common import WhaleSightingSerializer
from .serializers.populated import PopulatedWhaleSightingSerializer

# /whalesightings/
class WhaleSightingListView(APIView):

    # * Index
    def get(self, request):
        sightings = WhaleSighting.objects.all()
        serialized_sightings = PopulatedWhaleSightingSerializer(sightings, many=True)
        return Response(serialized_sightings.data)

    # * Create
    def post(self, request):
        pass