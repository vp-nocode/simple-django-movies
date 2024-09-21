from django.shortcuts import render
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'films/index.html', {'movies': movies})

def add_movie(request):
    return render(request, 'films/add_movie.html')