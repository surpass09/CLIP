from django.urls import path
from otlk_micro.views import Outlook_Data  # Import the class-based view

urlpatterns = [
    path('post/JSON/', Outlook_Data.as_view(), name='post-json'),
]

