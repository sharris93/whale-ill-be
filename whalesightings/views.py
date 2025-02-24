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
        new_sighting = WhaleSightingSerializer(data=request.data)
        if new_sighting.is_valid():
            new_sighting.save()
            return Response(new_sighting.data, 201)
        return Response(new_sighting.errors, 422)