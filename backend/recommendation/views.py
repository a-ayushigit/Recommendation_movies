from django.shortcuts import render
from compress_pickle import  load
from .serializers import  Rec_ReviewSerializer ,  Rec_ListSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movies
import os 
import numpy as np 
from rest_framework_simplejwt.authentication import JWTAuthentication

file_path = os.path.join(os.path.dirname(__file__),'model' , 'similarity_matrix.pkl.lzma')
with open(file_path , 'rb') as f:
    similarity = load(f ,  compression="lzma")


# Create your views here.
class Rec_ReviewListCreate(generics.ListCreateAPIView):
    serializer_class = Rec_ReviewSerializer
    permission_classes = [IsAuthenticated] #cannot call the route until you are authenticated by JWT tokens 
    #ListCreateView is used to list all the reviews created by users and create one if already not created 

    #to get all the reviews  written by a specific user 
    def get_queryset(self):
        user = self.request.user
        return Rec_ReviewSerializer.objects.filter(author=user)
    #filters the review by field , gives the users of only those reviews 
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else :
            print(serializer.errors)
        #serializer checks if the data is accurate or not 

class Rec_ReviewDelete(generics.DestroyAPIView):
    
    serializer_class = Rec_ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Rec_ReviewSerializer.objects.filter(author=user)
    

class Rec_movies_list_view(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Rec_ListSerializer 
    
    def get(self , request ):
        movie = request.GET.get('movie')
        print(movie)
        if not movie:
            return Response({"error": "Movie not provided"}, status=400)

        # get the object called movie_obj for corresponding movie name
        try:
            movie_obj = Movies.objects.get(title = movie)
            movie_index = movie_obj.id
            similar_movies = list(enumerate(similarity[movie_index]))
            sorted_similar_movies = sorted(similar_movies , key = lambda x : x[1] , reverse = True)
            sorted_similar_movies = sorted_similar_movies[1:6]
            movie_indices = [i[0] for i in sorted_similar_movies]
            movies = Movies.objects.filter(id__in = movie_indices)
        except Movies.DoesNotExist:
            return Response({"error": "Movie not found"}, status=404)
        except Exception as e:
            print(e)
            return Response({"error": "Internal server error"}, status=500)
        
        
        recommended_movies = [{"id": movie.id, "title": movie.title} for movie in movies]
        return Response({"recommended_movies": recommended_movies}) 