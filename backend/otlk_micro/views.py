from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OutlookUserData, Event
from datetime import datetime

class Outlook_Data(APIView):

    def post(self, request):
        people = request.data.get("people", [])  # Extract data from request

        for user in people:
            name = user.get("name")
            last_name = user.get("last_name")
            email = user.get("email")
            events = user.get("events", [])

            # Create user record
            outlook_data, created = OutlookUserData.objects.get_or_create(
                email=email,
                defaults={
                    'first_name': name,
                    'last_name': last_name
                }
            )

            # Create event records and link them to the created user
            for event in events:
                try:
                    # Convert ISO formatted string to datetime
                    timestamp = datetime.fromisoformat(event.get("time"))
                except ValueError:
                    return Response({"error": "Invalid date format for event"}, status=status.HTTP_400_BAD_REQUEST)
                
                Event.objects.create(
                    title=event.get("title"),
                    timestamp=timestamp,
                    outlook_user=outlook_data  # Link the event to the created user
                )

        return Response({"message": "Data processed successfully"}, status=status.HTTP_201_CREATED)
