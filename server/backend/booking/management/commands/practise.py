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
            seat_plans=[]
            seat_types = ['Premium' , 'VIP' , 'Standard' , 'Fixed Back' , 'Premium Glider' , 'Individual Chairs']
            sections = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G']
            no_sections = random.randint(4 , 6)
            total_seats = 0

            # print(no_sections)
            for i in range(no_sections):
                seat_plan = {}
                seat_plan['rows'] = random.randint(2,3)
                seat_plan['cols'] = random.randint(18,24)
                seat_plan['no_seats'] = seat_plan['rows']*seat_plan['cols']
                total_seats += seat_plan['no_seats']
                seat_plan['section'] = sections[i]
                seat_plan['seat_type'] = seat_types[i]
                seat_plans.append(seat_plan)
            
            seat_arr['seat_plans'] = seat_plans

            Seat_Arrangement.objects.create(
                seat_arrangement = seat_arr,
                
                no_seats = total_seats
            )
            


                