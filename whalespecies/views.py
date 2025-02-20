from rest_framework.views import APIView # this is the view class itself that we subclass to create our own custom views
from rest_framework.response import Response # this is the response object that allows us to respond to a request, ending the RR cycle

# Serializers
from .serializers.common import WhaleSpeciesSerializer

# Models
from .models import WhaleSpecies

# Create your views here.


# * /whalespecies - GET index, POST create
class SpeciesListView(APIView):

    # GET index route
    def get(self, request):
        # 1. Query the database table for all entries
        whales_queryset = WhaleSpecies.objects.all()
        # 2. Serialize the data that came from the database in order to send it back to the client
        whales_serialized = WhaleSpeciesSerializer(whales_queryset, many=True)
        # 3. Send the serialized data back to the client
        return Response(whales_serialized.data)

    # POST create route
    def post(self, request):
        return Response('HIT CREATE ROUTE')





# * /whalespecies/:id - GET show, PUT update, DELETE delete
class SpeciesDetailView(APIView):
    pass