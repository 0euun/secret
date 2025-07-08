from django.db import models
from django.utils import timezone

# Create your models here.
LANGUAGE_CHOICES = (
    (1, "KOR"),
    (2, "ENG"),
)

# post (자유글)
class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date published', default=timezone.now)
    body = models.TextField()
    language = models.IntegerField(choices=LANGUAGE_CHOICES, null=True)

    def __str__ (self):
        return self.title