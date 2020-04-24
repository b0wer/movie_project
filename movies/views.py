from django.shortcuts import render, redirect
from .models import Movie
from django.views.generic import View, DetailView, ListView
from .forms import ReviewForm


# Create your views here.
class List_Movie(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class DetailMovie(DetailView):
    model = Movie
    slug_field = 'url'


class AddReview(View):
    # Отзывы
    def post(self, request, pk):
        movie = Movie.objects.get(id=pk)
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent_id', None):
                form.parent_id = int(request.POST['parent_id'])
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
