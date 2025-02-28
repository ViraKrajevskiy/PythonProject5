
from django.shortcuts import render
from configapp.models import *

def index(request):
    actor = Actor.objects.all()
    movie = Movie.objects.all()

    context = {
        "actor":actor,
        "movie":movie,
    }
    return render(request,'index.html',context)

def get_movie(request,movie_id):
    movies = Movie.objects.all()
    movie = Movie.objects.get(pk=movie_id)
    actor = movie.actors.all()



    context = {
        "actor":actor,
        "movies":movies,
        "movie":movie,
    }
    return render(request,'film_janr.html',context)

def about_actor(request,actor_id):
    movie = Movie.objects.all()
    actor = Actor.objects.get(pk=actor_id)



    context = {
        "actor":actor,
        "movie":movie,
    }
    return render(request,'about.html',context)
def all_movies(request):
    movie = Movie.objects.all()




    context = {

        "movie":movie,
    }
    return render(request,'all_movies.html',context)



