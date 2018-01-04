from django.db import models
from django.core.validators import MinValueValidator


class Species(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Sighting(models.Model):
    # TODO: check that only allowed datetime format allowed
    dateTime = models.DateTimeField()
    description = models.TextField(max_length=500)
    species = models.ForeignKey(Species, to_field="name", on_delete=models.CASCADE, null=True)
    count = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.species.name + " " + str(self.date_time)
