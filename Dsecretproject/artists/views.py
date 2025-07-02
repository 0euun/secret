from django.shortcuts import render, redirect
from django.contrib.auth.forms import *
from artists. forms import *
from .models import *

def artist_main(request):
    artist = Artist.objects.first()
    return render(request, 'artist_main.html', {'artist': artist})

def artist_edit(request):
    artist = Artist.objects.first()
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artists:artist_main')
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'artist_edit.html', {'form': form})