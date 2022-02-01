"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
#
#
# from movies.views import *
# from movies.urls import *
# from django.urls import path, include

# urlpatterns = [

        # path('admin/', admin.site.urls),
        # #path('', views.home, name='core-home'),
        # path('', views.index),
        # path('movies', views.MovieList.as_view(), name='movies-list'),
        # path('movies/top/', views.TopMovies.as_view(), name='top10-movies'),
        # path('movies/<int:pk>', views.MovieDetail.as_view(), name='movies-detail'),
        # path('movie/<int:movie_id>/vote', views.CreateVote.as_view(), name='create-vote'),
        # path('movie/<int:movie_id>/vote/<int:pk>', views.UpdateVote.as_view(), name='update-vote'),


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from movies.urls import *
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),
    path('accounts/', include('django.contrib.auth.urls')),



]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


