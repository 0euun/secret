from django.db import models
from django.utils import timezone
from api.models import User
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
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    language = models.IntegerField(choices=LANGUAGE_CHOICES, null=True)

    def __str__ (self):
        return self.title