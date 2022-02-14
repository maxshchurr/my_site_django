from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import viewsets
from movies.models import Movie, Vote
from .serializers import MovieSerializer, VoteSerializer


class ListMovie(viewsets.ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        return queryset

    def post_queryset(self, serializer):
        try:
            serializer.save()
        except Exception as exc:
            print(exc)


class TopMovies(viewsets.ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.top_movies(limit=10)
        return queryset


class TopMoviesLimited(ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.top_movies()[:self.kwargs["limit"]]
        # serializer = MovieSerializer(queryset, many=True)
        return queryset



class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def update(self, request, parent_lookup_movie_id, pk=None):
        pk = parent_lookup_movie_id
        queryset = Vote.objects.api_get(pk)

        serializer = VoteSerializer(queryset, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)








