from django.db import models
from recommendation.models import Movies
# Create your models here.

## Movie , Show , Theatre , Seat , Reservation , Payment 

class Show (models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    theatre = models.ForeignKey('Theatre', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    price = models.IntegerField()
    status = models.BooleanField(default=True)
    type = models.CharField(max_length=100)
    available_seats = models.IntegerField()
    booked_seats = models.IntegerField()
    total_seats = models.IntegerField()
    place = models.CharField(max_length=900)
    

    def __str__(self):
        return self.movie +"-"+ self.theatre

class Theatre (models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    capacity = models.IntegerField()
    theatre_description = models.TextField()
    place = models.CharField(max_length=900)
    


    def __str__(self):
        return self.theatre_name
    
class SeatType(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()

    def __str__(self):
        return self.name

class Seat (models.Model):
    seat_number = models.IntegerField()
    theatre = models.ForeignKey(Theatre , on_delete=models.CASCADE)
    price = models.DecimalField( decimal_places=2 , max_digits=4)
    seat_type = models.ForeignKey(SeatType , on_delete=models.CASCADE , null=True, blank=True)

    def __str__(self):
        return f"{self.seat_number} ({self.theatre.name})"
    
class Reservation (models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat)
    status = models.BooleanField(default=True)
    payment_id = models.CharField(max_length=255)

class Payment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10 , decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
                                    




