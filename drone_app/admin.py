from django.contrib import admin
from drone_app.models import Location
from drone_app.models import DroneData


# Register your models here.
admin.site.register(Location)
admin.site.register(DroneData)