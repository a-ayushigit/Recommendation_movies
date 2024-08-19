from . import views 
from rest_framework.routers import DefaultRouter
from django.urls import path , include
router = DefaultRouter()

router.register("shows/" , views.Show_list_view , basename="shows")
router.register("seats/" , views.SeatView , basename="seats")
router.register("movies/" , views.Theatre_Movies_list_view , basename="theatre_movies")
router.register("theatre/" , views.Theatre_list_view , basename="theatres")
router.register("seat-type/", views.SeatTypeView, basename="seat-type")
router.register("seat/", views.SeatView, basename="seat")
router.register("reservation" , views.ReservationView, basename="reservation")
urlpatterns = [
    path('', include(router.urls) ),

]
