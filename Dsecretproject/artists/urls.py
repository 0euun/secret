from django.urls import path
from .views import *

app_name = 'artists'

urlpatterns = [
    path('', artist_main, name='artist_main'),
    path('edit/', artist_edit, name='artist_edit'),
]