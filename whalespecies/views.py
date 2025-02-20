from rest_framework.views import APIView # this is the view class itself that we subclass to create our own custom views
from rest_framework.response import Response # this is the response object that allows us to respond to a request, ending the RR cycle

# Create your views here.


# * /whalespecies - GET index, POST create
class SpeciesListView(APIView):

    # GET index route
    def get(self, request):
        return Response('HIT INDEX ROUTE')

    # POST create route
    def post(self, request):
        return Response('HIT CREATE ROUTE')





# * /whalespecies/:id - GET show, PUT update, DELETE delete
class SpeciesDetailView(APIView):
    pass