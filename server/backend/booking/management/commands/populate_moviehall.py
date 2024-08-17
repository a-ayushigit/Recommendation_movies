import random 
from datetime import timedelta , datetime 
from faker import Faker 
from django.core.management.base import BaseCommand
from booking.models import Show , Theatre , Payment , Reservation , SeatType , Seat , Movies,Seat_Arrangement, MovieHall, TheatreMovie , SeatId



class Command(BaseCommand):
    help = 'Populate the database with mock data'
    def handle(self , *args , **kwargs):
        fake = Faker('en_IN')

        no_movie_halls = random.randint(2, 5)
        for theatre in Theatre.objects.all():
             for _ in range(no_movie_halls):
                id = fake.uuid4()
                theatre = theatre
                name = str(theatre.id)+fake.ssn()
                seat_arrangement = Seat_Arrangement.objects.order_by('?').first()
                capacity = seat_arrangement.no_seats
                description = fake.paragraph(nb_sentences=40)
                MovieHall.objects.create(
                    id=id,
                    theatre=theatre,
                    name=name,
                    description=description,
                    capacity=capacity,
                    seat_arrangement=seat_arrangement
                )


        self.stdout.write(self.style.SUCCESS('Successfully populated the database with mock moviehall data'))
        
        