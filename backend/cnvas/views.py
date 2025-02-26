from django.shortcuts import render
from .models import CanvasUserData, Event
# Create your views here.



def post(self, request):

    if request.method == 200:
        people = request.data.get("people", [])
        for user in people:
            CanvasUserData.objects.create(
                
            )
            



    


