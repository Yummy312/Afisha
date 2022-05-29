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
