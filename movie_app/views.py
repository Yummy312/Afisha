from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Review, Director, Movie
from .serializers import MovieSerializers, DirectorSerializers, ReviewSerializers

#movie
@api_view(['GET'])
def show_movie_list(request):
    movie = Movie.objects.all()
    data = MovieSerializers(movie, many=True).data
    return Response(data=data)


@api_view(['GET'])
def show_detail_movie(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data=f'Not found {id}th page')
    data = MovieSerializers(movie).data
    return Response(data=data)

# director
@api_view(['GET'])
def show_director_list(request):
    director = Director.objects.all()
    data = DirectorSerializers(director, many=True).data
    return Response(data=data)


@api_view(['GET'])
def show_detail_director(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data=f'Not found {id}th page')
    data = DirectorSerializers(director).data
    return Response(data=data)


# review
@api_view(['GET'])
def show_review_list(request):
    review = Review.objects.all()
    data = ReviewSerializers(review, many=True).data
    return Response(data=data)


@api_view(['GET'])
def show_detail_review(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data=f'Not found {id}th page')
    data = ReviewSerializers(review).data
    return Response(data=data)






