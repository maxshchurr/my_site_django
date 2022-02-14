from rest_framework import serializers
from movies.models import Movie, Vote


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    year = serializers.IntegerField(min_value=0)

    class Meta:
        model = Movie
        fields = ['title', 'plot', 'year', 'rating']



class VoteSerializer(serializers.HyperlinkedModelSerializer):
    value = serializers.IntegerField(min_value=-1000)
    movie_id = serializers.IntegerField(min_value=0)

    class Meta:
        model = Vote
        fields = ['value', 'movie_id']






# from rest_framework import serializers
# from movies.models import Movie
#
# class AllMovieSerializers(serializers.ModelSerializer):
#     # title = serializers.CharField(required = True)
#     # data = serializers.CharField(required = True)
#     class Meta:
#         model = Movie
#         fields = ['title', 'plot', 'year', 'rating']
#
# class MovieRateSerializers (serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = [
#             'id', 'title', 'rating'
#         ]