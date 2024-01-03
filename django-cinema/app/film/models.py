from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg

from user.models import User


# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    short_description = models.TextField()
    description = models.TextField()
    direction = models.CharField(max_length=255)
    cast = models.TextField()
    scenario = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.title


class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.FloatField(
        validators=[
            MaxValueValidator(limit_value=10.0),
            MinValueValidator(limit_value=0.0)
        ]
    )

    def __str__(self):
        return f'{self.film}, {self.user}, {self.rating}'
