from rest_framework import serializers
from .models import OutlookUserData, Event


class OutlookDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = OutlookUserData
        fields = ['first_name', 'last_name', 'events', 'timings']

class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['events', 'user', 'timings']
        

