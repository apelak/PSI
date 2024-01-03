from .models import Film, Review
from rest_framework import serializers


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user']

