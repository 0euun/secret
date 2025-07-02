from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=50)
    team = models.CharField(max_length=200)
    birthday = models.DateField()
    position = models.CharField(max_length=100)
    # profile = models.ImageField() 추후 수정

    def __str__(self):
        return self.name