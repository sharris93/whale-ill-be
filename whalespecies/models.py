from django.db import models

STATUSES = [
    ("LC", "Least Concern"),
    ("NT", "Near Threatened"),
    ("VU", "Vulnerable"),
    ("EN", "Endangered"),
    ("CR", "Critically Endangered"),
    ("EW", "Extinct in the Wild"),
    ("EX", "Extinct"),
]

# Create your models here.
class WhaleSpecies(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100, blank=True, null=True) # a combination of blank=True & null=True allows us to make a field NOT required
    conservation_status = models.CharField(max_length=50, choices=STATUSES) # 'choices' allows us to pre-define the allowed values for a given field

    def __str__(self):
        return self.name