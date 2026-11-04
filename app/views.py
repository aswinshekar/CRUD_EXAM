from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app import serializers
from app.models import Vehicle
from app.serializers import VehicleSerializers
# Create your views here.

class VehicleCreate(APIView):
    def post(self,request):
        serializers_instance=VehicleSerializers(data=request.data)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class VechicleList(APIView):
    def get(self,request):
        qs=Vehicle.objects.all()
        serializers_instance=VehicleSerializers(qs,many=True)
        return Response(serializers_instance.data,status=status.HTTP_200_OK)

class VechicleView(APIView):
    def get(self,request,i):
        e=get_object_or_404(Vehicle,id=i)
        serializers_instance=VehicleSerializers(e)
        return Response(serializers_instance.data,status=status.HTTP_200_OK)
class VehicleUpdate(APIView):
    def put(self,request,i):
        e = get_object_or_404(Vehicle, id=i)
        serializers_instance = VehicleSerializers(instance=e,data=request.data)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers_instance.errors,status=status.HTTP_400_BAD_REQUEST)
class VehiclePartialUpdate(APIView):
    def patch(self,request,i):
        e = get_object_or_404(Vehicle, id=i)
        serializers_instance = VehicleSerializers(instance=e,data=request.data,partial=True)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class VehicleDelete(APIView):
    def delete(self, request, i):
        e = get_object_or_404(Vehicle, id=i)
        e.delete()
        return Response({"message":"DELETED"},status=status.HTTP_204_NO_CONTENT)




