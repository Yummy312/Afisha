from rest_framework import serializers
from .models import Review, Director, Movie


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class DirectorCountSerializer(serializers.ModelSerializer):
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'movie_count'.split()

    def get_movie_count(self, movie):
        return movie.all().count()
