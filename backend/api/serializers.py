#settings for JWT Tokens 
#convert json data to python objects and python objects to json data 

from django.contrib.auth.models import User
from rest_framework import serializers 
from .models import Review

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User 
        fields = ['id' , 'username' , 'password']
        extra_kwargs = {"password" :{"write_only" : True}} #we will accept password but will not return it , noone can read the password 

    def create(self , validated_data):
        user = User.objects.create_user(**validated_data)
        return user 
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta :
        model = Review 
        fields = ['id' , 'title' , 'content' , 'created_at' , 'author']
        extra_kwargs = {"author" : {"read_only":True}}#we will read who the author is but we will not write who the author is 
        