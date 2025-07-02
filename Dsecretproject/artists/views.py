from django.shortcuts import render, get_object_or_404
from .models import *

def artist_main(request):
    artist = Artist.objects
    return render(request, 'aritst.html', {'artist': artist})