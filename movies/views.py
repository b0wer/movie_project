from django.shortcuts import render
from .models import Movie
from django.views.generic import View, DetailView, ListView


# Create your views here.
class List_Movie(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class DetailMovie(DetailView):
    model = Movie
    slug_field = 'url'