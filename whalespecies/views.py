from rest_framework.views import APIView # this is the view class itself that we subclass to create our own custom views
from rest_framework.response import Response # this is the response object that allows us to respond to a request, ending the RR cycle

# Serializers
from .serializers.common import WhaleSpeciesSerializer

# Models
from .models import WhaleSpecies

# Create your views here.


# * /whalespecies - GET index, POST create
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





# * /whalespecies/:id - GET show, PUT update, DELETE delete
class SpeciesDetailView(APIView):
    pass