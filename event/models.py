from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField()
    priority = models.CharField(choices=[("low", "Low"), ("medium", "Medium"), ("high", "High")], default="medium")

    def __str__(self):
        return self.title
