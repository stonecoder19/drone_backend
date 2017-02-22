from django.shortcuts import render
from django.shortcuts import render_to_response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drone_app.serializers import LocationSerializer
from drone_app.models import Location
from drone_app.serializers import DroneDataSerializer
from drone_app.models import DroneData


# Create your views here.



class LocationView(APIView):

	def get(self,request,format=None):
		location = Location.objects.latest('id')
		serializer = LocationSerializer(location,many=False)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = LocationSerializer(data=request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DroneDataView(APIView):
	def get(self,request,format=None):

		data = DroneData.objects.all()
		serializer = DroneDataSerializer(data,many=True)
		return Response(serializer.data)

	def post(self,request,format=None):
		serializer = DroneDataSerializer(data=request.data)
		if(serializer.is_valid()):
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class DroneDataLatestView(APIView):

	def get(self,request,format=None):
		drone_data = DroneData.objects.latest('id')
		serializer = DroneDataSerializer(drone_data,many=False)
		return Response(serializer.data)








