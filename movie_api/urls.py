from django.urls import include, path
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedDefaultRouter

from . import views
from .views import TopMoviesLimited

router = routers.SimpleRouter()

router.register(r'movies', views.ListMovie, basename="ListMovie")
router.register(r'top', views.TopMovies, basename="TopMovies")
router.register(r'vote', views.VoteViewSet, 'movies-vote')

app_name = "movie_api"


urlpatterns = [

    path('', include(router.urls)),
    path('movies/top/<int:limit>', TopMoviesLimited.as_view(), name='top-movies-limited'),

]
urlpatterns += router.urls