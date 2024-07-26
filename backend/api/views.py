from django.shortcuts import render
from django.contrib.auth.models import User 
from rest_framework import generics 

from .serializers import UserSerializer 
from rest_framework.permissions import  AllowAny 

import pickle 
# with open('backend\api\model\similarity_matrix.pkl', 'rb') as f:
#     similarity = pickle.load(f)
# with open('backend\api\model\knn_model_small.pkl','rb') as f:
#     knn_model = pickle.load(f)
# with open('backend\api\model\corr_matrix_small.pkl','rb') as f:
#     corr_matrix = pickle.load(f)

# Create your views here.

#create a new user from registration form
# generics avoid repetition of code and allow to quickly build api views that map closely to database models 




class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()#list of all the objects to look at before creating a user to avoid creating an already existing user 
    serializer_class = UserSerializer #it tells the kind of data to use for making a new user 
    permission_classes = [AllowAny]


    
