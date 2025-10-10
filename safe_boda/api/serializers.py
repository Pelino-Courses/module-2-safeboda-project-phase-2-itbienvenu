from rest_framework import serializers
from .models import CustomUser, Trip


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__' # to serialize all fields in customer model


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__' # same here we serialize all fields in Trip model


class TripSerializer(serializers.ModelSerializer):
    rider = UserSerializer(read_only=True)
    driver = UserSerializer(read_only=True)

    class Meta:
        model = Trip
        fields = '__all__'