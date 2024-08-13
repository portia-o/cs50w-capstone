from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Habit(models.Model):
    class typ(models.TextChoices):
        GRATITUDE = "Gratitude"
        MEDITATION = "Meditation"
        EXERCISE = "Exercise"
        MUSIC = "Music"
        READ = "Read"
        KNIT = "Knit"
        OTHER = "Other"

    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="habits")
    h_type = models.CharField(max_length=32, choices=typ)
    notes = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}: {self.h_type} at {self.timestamp}"
    
