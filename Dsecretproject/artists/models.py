from django.db import models

class Artist(models.Model):
    profile = models.ImageField(upload_to='artist_photo', blank=True, null=True)
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=200)
    birthday = models.DateField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name