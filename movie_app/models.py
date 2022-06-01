from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=40)

    @property
    def movies_count(self):
        return self.movie_set.all().count()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True)
    duration = models.TimeField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def reviews(self):
        reviews = Review.object.filter(movie=self)
        return [{'text'} for i in reviews]

    @property
    def rating(self):
        r = 0
        for i in self.reviews.all():
            r += int(i.star)
        thing = r/self.reviews.all().count
        return thing


class Review(models.Model):
    star = [
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5)
    ]
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    stars = models.CharField(choices=star, max_length=100)

    def __str__(self):
        return self.movie.title

