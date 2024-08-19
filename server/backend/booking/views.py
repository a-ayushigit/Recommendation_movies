from django.shortcuts import render
from rest_framework.response import Response
from .serializers import  ShowSerializer , SeatSerializer , ReservationSerializer , TheatreSerializer , MoviesSerializer , SeatTypeSerializer , TheatreMovieSerializer
from rest_framework import viewsets
from .models import Show , Movies , Reservation , Payment , SeatType , Seat , Theatre , TheatreMovie
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ShowFilters , TheatreFilters , TheatreMovieFilters
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime
from django.utils.dateparse import parse_date
from rest_framework.exceptions import ValidationError
# Create your views here.

class Show_list_view(viewsets.ModelViewSet):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShowFilters
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     date_str = self.request.query_params.get('date')
    #     print(date_str)
    #     if date_str:
    #         parsed_date = self.parse_custom_date(date_str)
    #         print(parsed_date)
    #         if not parsed_date:
    #             raise ValidationError({'date': 'Invalid date format. Use YYYY-MM-DD or DD-MM-YYYY.'})
    #         queryset = queryset.filter(date=parsed_date)
    #         print(queryset[0])
            
    #     return queryset

    # def parse_custom_date(self, date_str):
    #     date = parse_date(date_str)
    #     if date:
    #         return date
    #     try:
    #         return datetime.strptime(date_str, '%d-%m-%Y').date()
    #     except ValueError:
    #         return None

class Theatre_list_view(viewsets.ModelViewSet):
    serializer_class = TheatreSerializer
    queryset = Theatre.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TheatreFilters

class Theatre_Movies_list_view(viewsets.ModelViewSet):
    serializer_class = TheatreMovieSerializer
    queryset = TheatreMovie.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TheatreMovieFilters

class SeatView(viewsets.ModelViewSet):
    serializer_class = SeatSerializer
    queryset = Seat.objects.all()

    def get(self , request):
        theatre_id = self.request.query_params.get('theatre_id')
        try:
            theatre = Theatre.objects.get(id = theatre_id)
            seats = Seat.objects.filter(theatre = theatre)
        except (Seat.DoesNotExist | Theatre.DoesNotExist) as e:
            print(e)
            return Response({"error":"Expected Resource not found"} , status=404)
        except Exception as e :
            print(e)
            return Response({"error":"Internal server error"} , status=500)
        
        return Response({"seats": seats} , status=200)
            
class SeatTypeView(viewsets.ModelViewSet):
    serializer_class = SeatTypeSerializer
    queryset = SeatType.objects.all()


class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail = False , methods=['POST'] ,url_path="reserve")
  
    def reserve_seat(self, request ):
        user = self.request.user
        theatre = self.request.theatre
        show_id = self.request.get('show_id')
        seat_ids = self.request.get('seat_id' , [])#gets a list of seat ids 
        if not seat_ids :
             return Response({"error": "No seats selected"}, status=400)
        

        with  transaction.atomic():
            try:
                show = Show.objects.select_for_update().get(id = show_id)
            

                if show.DoesNotExist:
                    return Response({"error":"Show not found"} , status=404)
                if show.status == False:
                    return Response({"error":"Show not available now"})
                
                reserved_seats = []
                for seat_id in seat_ids:
                  try:
                    seat = Seat.objects.select_for_update().get(seat_id = seat_id)
                  except seat.DoesNotExist:
                      return Response({"error":"Seat not found"} , status=404)
                  if Reservation.objects.filter(show=show , seat=seat , status=True).exists():
                      return Response({"error" : f"Seat {seat.seat_number} already reserved"} , status=400)
                  
                  reserved_seats.append(seat)
            
                reservation = Reservation.objects.create(user=user , show=show , payment_id='', seats=reserved_seats , theatre = theatre)
                reservation.seats.set(reserved_seats)
                reservation.save()
            except Exception as e :
                print(e)
                return Response({"error":"Internal server error"} , status=500)
        return Response({"reservation_id":reservation.id , "reservation details" : reservation} , status=201)
    def calculate_price(self,reservation_id):
        reservation = Reservation.objects.get(id=reservation_id)
        total_price = 0
        for seat in reservation.seats.all():
            total_price += seat.price
        return total_price
    
    def cancel_reservation(self , reservation_id):
        reservation = Reservation.objects.get(id=reservation_id)
        if reservation.status == False:
            return Response({"error":"Reservation already cancelled"} , status=400)
        reservation.status = False
        reservation.save()
        return Response({"message":"Reservation cancelled"} , status=200)