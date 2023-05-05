from rest_framework import serializers
from .models import Director, Film


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name')


class FilmSerializer(serializers.ModelSerializer):
    directors = DirectorSerializer(many=True)

    class Meta:
        model = Film
        fields = ('id', 'title', 'year', 'directors')
