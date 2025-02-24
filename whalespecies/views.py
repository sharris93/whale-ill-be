from rest_framework.views import APIView # this is the view class itself that we subclass to create our own custom views
from rest_framework.response import Response # this is the response object that allows us to respond to a request, ending the RR cycle
from rest_framework.exceptions import NotFound # This is the NotFound exception we can raise to send a 404

# Serializers
from .serializers.common import WhaleSpeciesSerializer

# Models
from .models import WhaleSpecies

# Create your views here.


# * /whalespecies/
class SpeciesListView(APIView):

    # * GET index route
    def get(self, request):
        whales_queryset = WhaleSpecies.objects.all()
        whales_serialized = WhaleSpeciesSerializer(whales_queryset, many=True)
        return Response(whales_serialized.data)


    # * POST create route
    def post(self, request):
        whale_serializer = WhaleSpeciesSerializer(data=request.data)

        if whale_serializer.is_valid():
            whale_serializer.save()
            return Response(whale_serializer.data, 201)
        
        return Response(whale_serializer.errors, 422)





# * /whalespecies/:whale_id/
class SpeciesDetailView(APIView):

    # * This method will be responsible for either sending a 404 or returning the found whale object
    def get_object(self, whale_id):
        try:
            whale = WhaleSpecies.objects.get(id=whale_id)
            return whale
        except WhaleSpecies.DoesNotExist as e:
            print(e)
            raise NotFound('Species not found.')
        
    
    # * GET show route
    def get(self, request, whale_id):
        whale = self.get_object(whale_id)
        serialized_whale = WhaleSpeciesSerializer(whale)
        return Response(serialized_whale.data)
    

    # * PUT update route
    def put(self, request, whale_id):
        whale = self.get_object(whale_id)
        serialized_whale = WhaleSpeciesSerializer(whale, data=request.data, partial=True)
        
        if serialized_whale.is_valid():
            serialized_whale.save()
            return Response(serialized_whale.data)
        
        return Response(serialized_whale.errors, 422)
            

    # * DELETE delete route
    def delete(self, request, whale_id):
        whale = self.get_object(whale_id)
        whale.delete()
        return Response(status=204)