from django.urls import path
from .views import SpeciesListView, SpeciesDetailView

# This acts as our router file for the whalespecies resource
# This is similar to our app.use('/', destinationRouter)

# * Every request that hits this "router", starts with:
# * /whalespecies
urlpatterns = [
    path('', SpeciesListView.as_view()), # path: /whalespecies
    path('<int:whale_id>/', SpeciesDetailView.as_view()) # path: /whalespecies/:whale_id
]