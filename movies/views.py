from django.shortcuts import render
from .models import Movie
from django.views.generic import View, DetailView


# Create your views here.
class List_Movie(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movie_list.html', {'movies': movies})
