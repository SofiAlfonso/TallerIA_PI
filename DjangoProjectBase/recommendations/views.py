from django.shortcuts import render
from movie.models import Movie
from .management.commands.movie_recommendations import Command
# Create your views here.

def recommendations(request):
    req = request.GET.get('searchMovie') # GET se usa para solicitar recursos de un servidor
    if req:
        movie=Command.handle(req, Command.handle)
        movies = Movie.objects.filter(title__icontains=movie)
    else:
        movies= None

    return render(request, 'recommendations.html', {'movies':movies, 'req': req}) 
    