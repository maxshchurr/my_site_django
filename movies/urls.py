from django.urls import path

from . import views

urlpatterns = [

    path('movies', views.MovieList.as_view(), name='movie-list'),
    path('movies/top', views.TopMovies.as_view(), name='top-movies'),
    path('movies/top/<int:limit>', views.top_movies_limited, name='top-movies-limited'),
    path('movies/<int:pk>', views.MovieDetail.as_view(), name='movie-detail'),
    path('movie/<int:movie_id>/vote', views.CreateVote.as_view(), name='create-vote'),
    path('movie/<int:movie_id>/vote/<int:pk>', views.UpdateVote.as_view(), name='update-vote'),
    #path('homepage/', views.home_page, name="home_page"),
    #path('login/', views.login_page, name="login_page")

]