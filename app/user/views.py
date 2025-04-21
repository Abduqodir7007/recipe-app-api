from django.shortcuts import render
from user.serializers import UserSerializer
from rest_framework import generics

class CreareUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    