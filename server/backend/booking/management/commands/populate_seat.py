import random 
from datetime import timedelta , datetime 
from faker import Faker 
from django.core.management.base import BaseCommand
from booking.models import Show , Theatre , Payment , Reservation , SeatType , Seat , Movies,Seat_Arrangement, MovieHall, TheatreMovie , SeatId



class Command(BaseCommand):
    help = 'Populate the database with mock data'
    def handle(self , *args , **kwargs):
        fake = Faker('en_IN')
        for movie_hall in MovieHall.objects.all():
          seat_number = 1
          theatre = movie_hall.theatre
          seat_arrangement = movie_hall.seat_arrangement

          for row in range(1, seat_arrangement.no_rows):
             for col in range(1,seat_arrangement.no_cols):
                Seat.objects.create(
                   theatre = theatre,
                   seat_arrangement = seat_arrangement,
                   status = False ,
                   seat_id = {
                      "row_num":row,
                      "col_num":col,
                      "seat_number":seat_number,
                      
                   }
                )
                

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with mock seat arrangement  data'))
        
        