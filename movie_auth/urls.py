from django.urls import path

from . import views

app_name = 'movie_auth'
urlpatterns = [

    path('', views.log_in, name='log_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.logout_from, name='log_out')

]