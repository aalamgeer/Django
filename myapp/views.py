# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Movie, Songs
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.http import HttpResponse


def index(request):
      all_movie = Movie.objects.all()
      context = {
         'all_movie': all_movie
      }
      return render(request, 'myapp/index.html', context)


def detail(request, movie_id):
   movie = get_object_or_404(Movie, pk=movie_id)
   return render(request, 'myapp/movie.html', {'movie': movie})


def favorite(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    try:
        selected_song = movie.songs_set.get(pk=request.POST['song'])
    except(keyError, Songs.DoesNotExist):
        return render(request, 'myapp/index.html', {'movie': movie, 'error_message': 'You did not select song'})
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'myapp/movie.html', {'movie': movie})
