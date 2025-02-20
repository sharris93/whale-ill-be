from rest_framework.views import APIView # this is the view class itself that we subclass to create our own custom views
from rest_framework.response import Response # this is the response object that allows us to respond to a request, ending the RR cycle
from rest_framework.exceptions import NotFound

# Serializers
from .serializers.common import WhaleSpeciesSerializer

# Models
from .models import WhaleSpecies

# Create your views here.


# * /whalespecies/ - GET index, POST create
class SpeciesListView(APIView):

    # * GET index route
    def get(self, request):
        # 1. Query the database table for all entries
        whales_queryset = WhaleSpecies.objects.all()
        # 2. Serialize the data that came from the database in order to send it back to the client
        whales_serialized = WhaleSpeciesSerializer(whales_queryset, many=True)
        # 3. Send the serialized data back to the client
        return Response(whales_serialized.data)

    # * POST create route
    def post(self, request):
        # 1. pass the request.data into the serializer for deserialization
        whale_serializer = WhaleSpeciesSerializer(data=request.data) # the data key is for data the will be added to the existing instance or used to create a new instance
        # 2. Check that the data was valid
        if whale_serializer.is_valid():
            # 3. If the data was valid, we will save the model and send the created object back to the client
            whale_serializer.save()
            return Response(whale_serializer.data, 201)
        
        # 4. If the data was invalid, we will send the errors back
        return Response(whale_serializer.errors, 422)





# * /whalespecies/:whale_id/ - GET show, PUT update, DELETE delete
class SpeciesDetailView(APIView):

    # This method will be responsible for either sending a 404 or returning the found whale object
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
        # 2. Serializer the whale data
        serialized_whale = WhaleSpeciesSerializer(whale)
        # 3. Send the serialized data back to the client
        return Response(serialized_whale.data)
    

    # * PUT update route
    def put(self, request, whale_id):
        # 1. Get the whale object
        whale = self.get_object(whale_id)

        # 2. Pass the instance above (whale) and the incoming data (request.data) into the serializer
        serialized_whale = WhaleSpeciesSerializer(whale, data=request.data, partial=True)
        
        # 3. Validate the incoming data
        if serialized_whale.is_valid():
            # 4. Save the instance
            serialized_whale.save()
            # 5. Return the updated instance back to the client
            return Response(serialized_whale.data)
        
        # 6. Send the errors back in a 422
        return Response(serialized_whale.errors, 422)
            

    # * DELETE delete route
    def delete(self, request, whale_id):
        whale = self.get_object(whale_id)
        whale.delete()
        return Response(status=204)