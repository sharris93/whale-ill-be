from rest_framework.serializers import ModelSerializer # Model serializer class
from ..models import WhaleSpecies # Model to base the serializer off

class WhaleSpeciesSerializer(ModelSerializer):
    class Meta:
        model = WhaleSpecies # This sets the model for the serializer
        fields = '__all__' # This defines the fields we want to include in serialization/deserialization



class WhaleSpeciesNameSerializer(ModelSerializer):
    class Meta:
        model = WhaleSpecies
        fields = ['name']