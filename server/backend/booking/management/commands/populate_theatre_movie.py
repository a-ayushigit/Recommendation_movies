import random 
from datetime import timedelta 
from faker import Faker 
from django.core.management.base import BaseCommand
from booking.models import Show , Theatre , Payment , Reservation , SeatType , Seat , Movies,Seat_Arrangement, MovieHall, TheatreMovie , SeatId



class Command(BaseCommand):
    help = 'Populate the database with mock data'
    def handle(self , *args , **kwargs):
        fake = Faker('en_IN')

        movie_halls = MovieHall.objects.all()
        
        for movie_hall in MovieHall.objects.all():
             for _ in range(5):
                release_date = fake.date_this_month()  # Define release_date here
                end_date = release_date + timedelta(days=random.randint(1, 25))  # Use release_date to calculate end_date   
                TheatreMovie.objects.create(
                      id=fake.uuid4(),
                      movie_hall=movie_hall,
                      theatre=movie_hall.theatre,
                      movie=Movies.objects.get(id=random.randint(1, 500)),
                      release_date=release_date,
                      end_date = end_date

                  )  

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with mock theatremovie data'))
        
        