from django.db import models
from whalespecies.models import WhaleSpecies
from users.models import User

# Create your models here.
class WhaleSighting(models.Model):
    species = models.ForeignKey(
        to=WhaleSpecies,
        on_delete=models.CASCADE, # Use models.CASCADE when you want this object to be deleted when the relation is deleted
        related_name='sightings'
    )
    longitude = models.FloatField()
    latitude = models.FloatField()
    date_sighted = models.DateTimeField(auto_now_add=True) # auto_now_add will give you a timestamp the first time the object is created
    behaviour = models.TextField(max_length=350)