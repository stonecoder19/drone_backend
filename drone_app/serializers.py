from rest_framework import serializers
from drone_app.models import Location
from drone_app.models import DroneData




class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = ('lat','lon','time')

class DroneDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = DroneData
		fields = ('lat','lon','accx','accz','accy','gyrx','gyry','gyrz','magx','magy','magz','est_alt','vario','rc_throttle','rc_pitch','rc_yaw','rc_roll','vbat','time');



