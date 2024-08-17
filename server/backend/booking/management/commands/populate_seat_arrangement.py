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
            seat_types = [' Premium' , 'VIP' , 'Standard' , 'Fixed Back' , 'Premium Glider' , 'Individual Chairs']
            no_rows = random.randint(20, 40)  # Random number of rows
            no_cols = random.randint(20, 40)  # Random number of columns
            no_seats =max(100, no_rows * no_cols)

            #Create a random seating arrangement for different movie halls 
            
            chosen_seat_types = random.sample(seat_types , 3)

            for seat in chosen_seat_types :
                if ((seat != 'Standard') and (seat != 'Individual chairs')) :
                    seat_arr[seat] = random.randint(5, no_seats // 10)
                
            if 'Standard' not in seat_arr:
                seat_arr['Standard'] = (no_seats - sum(seat_arr.values())) // 2
            if 'Fixed Back' not in seat_arr:
                seat_arr['Fixed Back'] = (no_seats - sum(seat_arr.values())) // 2

            total_assigned_seats = sum(seat_arr.values())
            if (total_assigned_seats > no_seats):
                seat_arr['Standard'] -= total_assigned_seats - no_seats
            elif (total_assigned_seats < no_seats):
                seat_arr['Standard'] += no_seats - total_assigned_seats

            

            for j in range(4):
                seat_type = seat_types[random.randint(0,5)]
                seat_arr[seat_type] = random.randint(5, no_seats // 2)
            
            Seat_Arrangement.objects.create(
                seat_arrangement = seat_arr,
                no_rows = no_rows,
                no_cols = no_cols,
                no_seats = no_seats
            )
            

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with mock seat arrangement  data'))
        
        