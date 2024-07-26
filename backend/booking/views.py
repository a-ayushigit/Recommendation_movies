from django.shortcuts import render
from rest_framework.decorators import api_view , action
from rest_framework.response import Response
from .serializers import MoviesSerializer , ShowSerializer , TheatreSerializer , SeatSerializer , ReservationSerializer , PaymentSerializer , SeatTypeSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Show , Reservation , Payment , Theatre , Seat , SeatType
from recommendation.models import Movies
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ShowFilters , TheatreFilters , MovieFilters
from rest_framework import viewsets
from django.db import transaction
# Create your views here.
# make booking 
# save data to database 


class Show_list_view(viewsets.ModelViewSet):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShowFilters


class Theatre_list_view(viewsets.ModelViewSet):
    serializer_class = TheatreSerializer
    queryset = Theatre.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TheatreFilters

    # def get(self , request):
    #     place = self.request.query_params.get('place')
    #     theatre = self.request.query_params.get('theatre')
    #     try:
    #         shows = Show.objects.filter(place=place , theatre=theatre)
    #     except Show.DoesNotExist:
    #         return Response({"error":"Place not found"} , status=404)
    #     except Exception as e :
    #         print(e)
    #         return Response({"error":"Internal server error"} , status=500)

    #     return Response({"shows": shows} , status=200)


class Movies_list_view(viewsets.ModelViewSet):
    serializer_class = MoviesSerializer
    queryset = Movies.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilters

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
    permission_classes = [IsAuthenticated]

    @action(detail = False , methods=['POST'] ,url_path="reserve")
  
    def reserve_seat(self, request ):
        user = self.request.user
        show_id = self.request.get('show_id')
        seat_ids = self.request.get('seat_id' , [])#gets a list of seat ids 
        if not seat_ids :
             return Response({"error": "No seats selected"}, status=400)
        

        with  transaction.atomic():
            try:
                show = Show.objects.select_for_update().get(id = show_id)
            

                if Show.DoesNotExist:
                    return Response({"error":"Show not found"} , status=404)
                if show.status == False:
                    return Response({"error":"Show not available now"})
                
                reserved_seats = []
                for seat_id in seat_ids:
                  try:
                    seat = Seat.objects.select_for_update().get(id = seat_id)
                  except Seat.DoesNotExist:
                      return Response({"error":"Seat not found"} , status=404)
                  if Reservation.objects.filter(show=show , seat=seat).exists():
                      return Response({"error" : f"Seat {seat.seat_number} already reserved"} , status=400)
                  
                  reserved_seats.append(seat)
            
                reservation = Reservation.objects.create(user=user , show=show , payment_id='')
                reservation.seats.set(reserved_seats)
                reservation.save()
            except Exception as e :
                print(e)
                return Response({"error":"Internal server error"} , status=500)
        return Response({"reservation_id":reservation.id} , status=201)
            
            
    
            
            
            
            
        



