from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import viewsets
from movies.models import Movie, Vote
from .serializers import MovieSerializer, VoteSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter


class SetPagination(PageNumberPagination):
    page_size = 20


class ListMovie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = SetPagination
    filterset_fields = ['year', 'title']
    ordering_fields = ['year', 'title']
    ordering = ['-year']

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
    pagination_class = SetPagination
    filterset_fields = ['year', 'title']
    ordering_fields = ['year', 'title']
    # ordering = ['-year']
    # ordering doest work with top movies cause of ' cannot reorder a query once a slice has been taken ' error

    def get_queryset(self):
        queryset = Movie.objects.top_movies(limit=10)
        return queryset


class TopMoviesLimited(ListAPIView):
    serializer_class = MovieSerializer
    pagination_class = SetPagination
    filterset_fields = ['year', 'title']
    ordering_fields = ['year', 'title']
    # ordering = ['-year']
    # ordering doest work with top movies cause of ' cannot reorder a query once a slice has been taken ' error

    def get_queryset(self):
        queryset = Movie.objects.top_movies()[:self.kwargs["limit"]]
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




