from django.urls import path 
from . import views 

urlpatterns = [
    path('rec_reviews/' , views.Rec_ReviewListCreate.as_view() , name='rec_review-list'),
    path('rec_reviews/delete/<int:pk>/' , views.Rec_ReviewDelete.as_view() , name='delete-rec_review'),
    path('rec_movies_list/' , views.Rec_movies_list_view.as_view() , name="movies-recommended-list")
    
]