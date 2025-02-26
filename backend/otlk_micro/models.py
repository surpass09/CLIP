from django.db import models

class OutlookUserData(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Event(models.Model):
    title = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    outlook_user = models.ForeignKey(OutlookUserData, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.title
    