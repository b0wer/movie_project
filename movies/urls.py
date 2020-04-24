from django.urls import path
from . import views

urlpatterns = [
    path('', views.List_Movie.as_view()),
    path('<slug:slug>', views.DetailMovie.as_view(), name='movie_detail'),
    path('addreview/<int:pk>', views.AddReview.as_view(), name='add_review')
]