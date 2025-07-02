from django import forms
from django.forms.widgets import ClearableFileInput
from .models import Artist

class NoClearableFileInput(ClearableFileInput):
    template_name = 'widgets/custom_file_input.html'
    
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        widgets = {
            'profile': NoClearableFileInput(),
        }
