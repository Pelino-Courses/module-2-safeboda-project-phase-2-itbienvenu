from rest_framework import serializers
from .models import CustomUser, Trip


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'user_type']

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            user_type=validated_data['user_type']
        )
        user.set_password(validated_data['password'])  # Hash password
        user.save()
        return user
    

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__' # same here we serialize all fields in Trip model


class TripSerializer(serializers.ModelSerializer):
    rider = UserSerializer(read_only=True)
    driver = UserSerializer(read_only=True)

    def validate(self, data):
        if data.get('rider') == data.get('driver'):
            raise serializers.ValidationError("Rider and driver cannot be the same user.")
        return data

    class Meta:
        model = Trip
        fields = '__all__'