import random 
from datetime import timedelta , datetime 
from faker import Faker 
from django.core.management.base import BaseCommand
from booking.models import Show , Theatre , Payment , Reservation , SeatType , Seat , Movies,Seat_Arrangement, MovieHall, TheatreMovie , SeatId



class Command(BaseCommand):
    help = 'Populate the database with mock data'
    def handle(self , *args , **kwargs):
        fake = Faker('en_IN')
        seat_types =[
  {
    "name": "Premium",
    "description": "Premium seats offer the ultimate comfort and luxury with spacious seating, plush cushioning, and advanced reclining features. Perfect for a high-end movie experience, these seats provide ample legroom and a personal armrest. Enjoy the movie with premium service and added amenities.",
    "price": 750.0
  },
  {
    "name": "VIP",
    "description": "VIP seats are designed for moviegoers who seek an elevated viewing experience. These seats come with extra cushioning, wider armrests, and additional legroom. Enjoy priority service and a more private and comfortable setting. Ideal for those who prefer a luxurious touch.",
    "price": 900.0
  },
  {
    "name": "Standard",
    "description": "Standard seats are the classic choice for moviegoers, offering a balance of comfort and affordability. These seats are well-cushioned and ergonomically designed to provide a pleasant viewing experience. Perfect for casual movie outings with family and friends.",
    "price": 300.0
  },
  {
    "name": "Fixed Back",
    "description": "Fixed Back seats provide a stable and comfortable seating option. With a non-reclining design, these seats ensure a consistent viewing angle and support. Ideal for those who prefer a traditional seating arrangement without the extra features of luxury seats.",
    "price": 250.0
  },
  {
    "name": "Premium Glider",
    "description": "Premium Glider seats combine luxury with motion, allowing you to gently glide back and forth for a more dynamic and relaxing experience. These seats are highly cushioned and provide advanced ergonomic support, making them perfect for long movie sessions.",
    "price": 850.0
  },
  {
    "name": "Individual Chairs",
    "description": "Individual Chairs offer personal space and comfort, with each chair designed to provide maximum support and cushioning. These chairs are perfect for those who prefer a more private and individualized movie experience, with added amenities and services.",
    "price": 650.0
  }
]

        for seat_type in seat_types:
            SeatType.objects.create(
                name = seat_type["name"],
                description = seat_type["description"],
                price = seat_type["price"]
            )

            
            

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with mock seat type data'))
        
        