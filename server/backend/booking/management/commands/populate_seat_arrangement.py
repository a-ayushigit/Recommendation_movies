import random 
from datetime import timedelta , datetime 
from faker import Faker 
from django.core.management.base import BaseCommand
from booking.models import Show , Theatre , Payment , Reservation , SeatType , Seat , Movies,Seat_Arrangement, MovieHall, TheatreMovie , SeatId



class Command(BaseCommand):
    help = 'Populate the database with mock data'
    def handle(self , *args , **kwargs):
        fake = Faker('en_IN')
        for i in range(20):
            seat_arr={}
            seat_types = ['premium' , 'VIP' , 'standard' , 'fixed back' , 'Premium Glider']
            no_rows = random.randint(5, 10)  # Random number of rows
            no_cols = random.randint(5, 10)  # Random number of columns
            no_seats = no_rows * no_cols
            for j in range(4):
                seat_type = seat_types.random.randint(0,5)
                seat_arr[seat_types[seat_type]] = random.randint(5, 15)
            Seat_Arrangement.objects.create(
                seat_arrangement = seat_arr,
                no_rows = no_rows,
                no_cols = no_cols,
                no_seats = no_seats
            )
            

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with mock seat arrangement  data'))
        
        