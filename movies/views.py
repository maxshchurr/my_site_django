from django.contrib.auth.mixins import (LoginRequiredMixin)
from django.core.exceptions import (PermissionDenied)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse

from .forms import VoteForm, MovieForm
from .models import Movie, Vote



class MovieList(ListView, ModelFormMixin):
    model = Movie
    form_class = MovieForm

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MovieList, self).get_context_data(**kwargs)

        context["movie_form"] = self.form
        return context


class MovieDetail(DetailView):
    queryset = Movie.objects.all_about_movie()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vote = Vote.objects.get_vote_or_unsaved_blank_vote(
            movie=self.object
        )
        if vote.id:
            vote_form_url = reverse(
                "update-vote", kwargs={"movie_id": vote.movie.id, "pk": vote.id}
            )
        else:
            vote_form_url = reverse(
                "create-vote", kwargs={"movie_id": self.object.id}
            )
        vote_form = VoteForm(instance=vote)
        context["vote_form"] = vote_form
        context["vote_form_url"] = vote_form_url

        return context


class TopMovies(ListView):
    template_name = "movies/top_movies.html"

    def get_queryset(self):
        limit = 10
        return Movie.objects.top_movies(limit=limit)


class TopMoviesLimited(ListView):
    template_name = "movies/top_movies.html"

    def get_queryset(self):
        queryset = Movie.objects.top_movies()[:self.kwargs['limit']]
        return queryset


class CreateVote(CreateView):
    form_class = VoteForm

    def get_initial(self):
        initial = super().get_initial()
        initial["movie"] = self.kwargs["movie_id"]
        return initial

    def get_success_url(self):
        movie_id = self.object.movie.id
        return reverse("movie-detail", kwargs={"pk": movie_id})

    def render_to_response(self, context, **response_kwargs):
        initial = super().get_initial()
        initial["movie"] = self.kwargs["movie_id"]
        movie_id = initial["movie"]
        movie_detail_url = reverse("movie-detail", kwargs={"pk": movie_id})
        return redirect(to=movie_detail_url)


class UpdateVote(UpdateView):
    form_class = VoteForm
    queryset = Vote.objects.all()

    def get_object(self, queryset=None):
        vote = super().get_object(queryset)
        return vote

    def get_success_url(self):
        movie_id = self.object.movie.id
        return reverse("movie-detail", kwargs={"pk": movie_id})

    def render_to_response(self, context, **response_kwargs):
        movie_id = self.object.id
        movie_detail_url = reverse("movie-detail", kwargs={"pk": movie_id})
        return redirect(to=movie_detail_url)






# def home_page(request):
#     return render(request, "users/home_page.html")
#
#
# def login_page(request):
#     return render(request, "registration/login.html")

