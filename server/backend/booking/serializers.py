from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import Show , Theatre , Payment , Reservation , SeatType , Seat , Movies,Seat_Arrangement, MovieHall, TheatreMovie , SeatId

class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = '__all__'

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
    class Meta:
        model = MovieHall
        fields = '__all__'

class TheatreMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreMovie
        fields = '__all__'

class SeatIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatId
        fields = '__all__'

class SeatTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatType
        fields = '__all__'