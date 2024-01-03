from rest_framework import serializers
from .models import Cinema_Hall, Showing, Ticket, Halls_Seats

class Cinema_HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema_Hall
        fields = '__all__'


class Halls_SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Halls_Seats
        fields = '__all__'


class ShowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showing
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


