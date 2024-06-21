from django.shortcuts import render
from django.contrib.auth.models import User 
from rest_framework import generics 
from .serializers import UserSerializer , ReviewSerializer
from rest_framework.permissions import IsAuthenticated , AllowAny 
from .models import Review

# Create your views here.

#create a new user from registration form
# generics avoid repetition of code and allow to quickly build api views that map closely to database models 

class ReviewListCreate(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated] #cannot call the route until you are authenticated by JWT tokens 
    #ListCreateView is used to list all the reviews created by users and create one if already not created 

    #to get all the reviews  written by a specific user 
    def get_queryset(self):
        user = self.request.user
        return Review.objects.filter(author=user)
    #filters the review by field , gives the users of only those reviews 
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else :
            print(serializer.errors)
        #serializer checks if the data is accurate or not 

class ReviewDelete(generics.DestroyAPIView):
    
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Review.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()#list of all the objects to look at before creating a user to avoid creating an already existing user 
    serializer_class = UserSerializer #it tells the kind of data to use for making a new user 
    permission_classes = [AllowAny]
