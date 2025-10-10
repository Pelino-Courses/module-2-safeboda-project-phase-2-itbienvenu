from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser, Trip

from .serializers import UserSerializer, TripSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
