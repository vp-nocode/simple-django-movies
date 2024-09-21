from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm, ReviewForm
from .models import Movie, Review


def index(request):
    movies = Movie.objects.all()
    return render(request, 'films/index.html', {'movies': movies})

def add_movie(request):
    error = None
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('home')
        else:
            error = "incorrect data"

    form = MovieForm()
    return render(request, 'films/add_movie.html', {'form': form})

def add_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'films/add_review.html', {'form': form, 'movie': movie})