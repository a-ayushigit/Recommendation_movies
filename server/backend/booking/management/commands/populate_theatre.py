import random 
from datetime import timedelta , datetime 
from faker import Faker 
from django.core.management.base import BaseCommand
from booking.models import Show , Theatre , Payment , Reservation , SeatType , Seat , Movies,Seat_Arrangement, MovieHall, TheatreMovie , SeatId



class Command(BaseCommand):
    help = 'Populate the database with mock data'
    def handle(self , *args , **kwargs):
        fake = Faker('en_IN')

        for _ in range(20):
            Theatre.objects.create(
                name = fake.company(),
                address = fake.street_address(),
                place = fake.city()
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with mock theatre data'))
        
        