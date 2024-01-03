from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import ForeignKey

from film.models import Film
from user.models import User


class Cinema_Hall(models.Model):
    hall_number = models.IntegerField(primary_key=True)
    hall_row = models.IntegerField(default=0)
    hall_col = models.IntegerField(default=0)


class Halls_Seats(models.Model):
    hall_number = models.ForeignKey(Cinema_Hall, on_delete=models.CASCADE)
    sit_number_row = models.IntegerField(default=1)
    sit_number_col = models.IntegerField(default=1)
    is_taken = models.BooleanField(default=False)

    def clean(self):
        if self.sit_number_row > self.hall_number.hall_row:
            raise ValidationError('Row number is greater than hall row number.')
        if self.sit_number_col > self.hall_number.hall_col:
            raise ValidationError('Column number is greater than hall column number.')


class Showing(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    time = models.DateTimeField()
    hall_number = models.ForeignKey(Cinema_Hall, on_delete=models.CASCADE)



class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showing = models.ForeignKey(Showing, on_delete=models.CASCADE)
    place = models.ForeignKey(Halls_Seats, on_delete=models.CASCADE)

    @property
    def film_price(self):
        return self.showing.film.price
