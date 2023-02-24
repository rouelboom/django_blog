from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    create_date = models.DateTimeField(default=timezone.now, blank=True)
    content = models.TextField()
    rating = models.IntegerField(default=0)

    ordering = ['create_date']

    def __str__(self):
        return self.title
