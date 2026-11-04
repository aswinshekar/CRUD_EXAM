from rest_framework import serializers
from app.models import Vehicle


class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model=Vehicle
        fields="__all__"

