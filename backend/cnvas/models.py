from django.db import models

# Create your models here.

class CanvasUserData(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.first_name} {self.email}"
    
class Event(models.Model):
    events = models.CharField(max_length=400)
    time = models.DateTimeField()
    canvas_user = models.ForeignKey(CanvasUserData, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.events}"
