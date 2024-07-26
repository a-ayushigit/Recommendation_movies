from django.urls import path , include
from . import views 
from rest_framework.routers import  DefaultRouter

router = DefaultRouter()

router.register(r'shows', views.Show_list_view)
router.register(r'theatres', views.Theatre_list_view)
router.register(r'make_reservations', views.ReservationView)

urlpatterns = [
    # path('list_show/' , views.Show_list_view.as_view() , name='show-list'),
    # path('list_theatre/' , views.Theatre_list_view.as_view() , name='theatre-list'),
    # path('make_reservation/' , views.ReservationView.as_view() , name="movies-reservation")

    path('' , include(router.urls)),
    
]