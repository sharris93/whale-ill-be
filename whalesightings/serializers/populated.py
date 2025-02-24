from .common import WhaleSightingSerializer
from whalespecies.serializers.common import WhaleSpeciesSerializer
from tags.serializers.common import TagSerializer

class PopulatedWhaleSightingSerializer(WhaleSightingSerializer):
    species = WhaleSpeciesSerializer()
    tags = TagSerializer(many=True)