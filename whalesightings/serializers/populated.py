from .common import WhaleSightingSerializer
from whalespecies.serializers.common import WhaleSpeciesSerializer

class PopulatedWhaleSightingSerializer(WhaleSightingSerializer):
    species = WhaleSpeciesSerializer()