from django.shortcuts import render


def index(request):
    return render(request, 'films/index.html')

def add_movie(request):
    return render(request, 'films/add_movie.html')