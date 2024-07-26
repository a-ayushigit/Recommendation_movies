from django.contrib.auth.models import User
from rest_framework import serializers 
from .models import Rec_Review , RecommendationList


class Rec_ReviewSerializer(serializers.ModelSerializer):
    class Meta :
        model = Rec_Review 
        fields = ['id' , 'title' , 'content' , 'created_at' , 'author']
        extra_kwargs = {"author" : {"read_only":True}}#we will read who the author is but we will not write who the author is 
        
class Rec_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationList
        fields = ['id' , 'user' , 'movies' , 'created_at']
        extra_kwargs = {"author" : {"read_only":True}}
