from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import Show , Theatre , Payment , Reservation , SeatType , Seat , Movies,Seat_Arrangement, MovieHall, TheatreMovie , SeatId
from django.db import models


class TheatreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theatre
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class SeatTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatType
        fields = '__all__'

class Seat_ArrangementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat_Arrangement
        fields = '__all__'

class MovieHallSerializer(serializers.ModelSerializer):
    seat_arrangement = Seat_ArrangementSerializer(read_only=True)
    class Meta:
        model = MovieHall
        fields = '__all__'

class TheatreMovieSerializer(serializers.ModelSerializer):
    movie = MoviesSerializer(read_only=True)
    movie_hall = MovieHallSerializer(read_only=True)
    theatre = TheatreSerializer(read_only=True)
    class Meta:
        model = TheatreMovie
        fields = ['id' , 'movie' , 'movie_hall' , 'theatre' , 'release_date' , 'end_date']

class ShowSerializer(serializers.ModelSerializer):
    theatre_movie = TheatreMovieSerializer(read_only=True)
    # date = models.DateField()
    class Meta:
        model = Show
        fields = ['id' , 'theatre_movie' , 'place' , 'start_time' , 'end_time' , 'status' , 'date']

class SeatIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatId
        fields = '__all__'

class SeatTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatType
        fields = '__all__'