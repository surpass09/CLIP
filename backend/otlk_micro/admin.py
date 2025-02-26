from django.contrib import admin
from otlk_micro.models import OutlookUserData, Event
# Register your models here.

admin.site.register(OutlookUserData)
admin.site.register(Event)