from django.db import models

from django.conf import settings



class Movie(models.Model):
    name = models.CharField(max_length=140)
    year = models.PositiveIntegerField(default=2000)
    runtime = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)
    actors = models.CharField(max_length=300, default='')

    #objects = MovieManager()
    def __str__(self):
        return "{} ({})year {}hr {}stars/10.\nActors: {}.".format(self.name, self.year, self.runtime, self.rating, self.actors)


class Actor(models.Model):
    name = models.CharField(max_length=140)
    age = models.PositiveIntegerField(default=20)

    def __str__(self):
        return "{}.{}years old".format(self.name, self.age)


# class Role(models.Model):
#     name = models.CharField(max_length=140)
#
#
#     #objects = MovieManager()
#     def __str__(self):
#         return "{}".format(self.name)