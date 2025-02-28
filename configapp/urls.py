from  django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',index,name='home'),
    path('',index,name='home'),
    path('movie_actors/<int:movie_id>',get_movie,name='get_movie'),
    path('actor/<int:actor_id>',about_actor,name='about_actor'),
    path('movie/',all_movies,name='all_movies'),
]