from .common import WhaleSpeciesSerializer
from whalesightings.serializers.common import WhaleSightingSerializer

class PopulatedWhaleSpeciesSerializer(WhaleSpeciesSerializer):
    sightings = WhaleSightingSerializer(many=True)