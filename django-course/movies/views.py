from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from movies.models import Movie

def home(request):
    return render(request, 'movies/home.html')

def about(request):
    return render(request, 'movies/about.html')

def movies(request):
    movies_list = Movie.objects.all()
    return render(request, 'movies/movies.html', {
        'movies_list':movies_list
    })

def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)

    return render(
        request,
        "movies/movie_detail.html",
        {"movie": movie}
    )