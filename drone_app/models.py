from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.



class Location(models.Model):
	name = models.CharField(max_length=255,default='test')
	lat  = models.CharField(max_length=255)
	lon  = models.CharField(max_length=255)
	time = models.DateTimeField('auto_now_add=true',default=timezone.now(),editable=False)

	def __str__(self):
		return self.name


class DroneData(models.Model):
	lat = models.CharField(max_length=255,default='0.0')
	lon = models.CharField(max_length=255,default='0.0')
	angx = models.CharField(max_length=255,default='0.0')
	angy = models.CharField(max_length=255,default='0.0')
	heading = models.CharField(max_length=255,default='0.0')
	accx = models.CharField(max_length=255,default='0')
	accy = models.CharField(max_length=255,default='0')
	accz = models.CharField(max_length=255,default='0')
	gyrx = models.CharField(max_length=255,default='0')
	gyry = models.CharField(max_length=255,default='0')
	gyrz = models.CharField(max_length=255,default='0')
	magx = models.CharField(max_length=255,default='0')
	magy = models.CharField(max_length=255,default='0')
	magz = models.CharField(max_length=255,default='0')
	est_alt = models.CharField(max_length=255,default='0')
	vario = models.CharField(max_length=255,default='0')
	rc_throttle = models.IntegerField(default=0)
	rc_pitch = models.IntegerField(default=0)
	rc_yaw = models.IntegerField(default=0)
	rc_roll = models.IntegerField(default=0)
	vbat = models.CharField(max_length=255,default=0)
	time = models.DateTimeField('auto_now_add=true',default=timezone.now(),editable=False)

	def __str__(self):
		return str(self.time)



