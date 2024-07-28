from django.shortcuts import render
#import the model 
from django.contrib.auth.models import User
from rest_framework import generics 

from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

# Create your views here.

class createUserView(generics.CreateAPIView):
    queryset = User.objects.all()#list of all the objects to look at before creating a user to avoid creating an already existing user 
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
