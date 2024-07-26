from django.db import models
from django.contrib.auth.models import User 

class Rec_Review(models.Model):
    title= models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name="rec_reviews")

    def __str__(self):
        return self.title

# class Genre(models.Model):
#     name = models.CharField(max_length=100)

class Movies(models.Model):
    title = models.TextField()
    movie_id = models.IntegerField(default=None)
    overview = models.TextField(default=None)
    genres = models.CharField(max_length=200 , null=True, blank=True)
    cast = models.TextField()
    crew = models.CharField(max_length=200 , null=True, blank=True)
    production_companies = models.TextField()
    runtime = models.IntegerField(default = 100)
    release_date = models.DateField(null = True , blank = True)
    

    def __str__(self):
        return self.title

class RecommendationList(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movies)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recommendation List for : {self.user.username}"
    
