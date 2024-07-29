from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movies(models.Model):
    title = models.CharField(max_length=255)
    movie_id = models.IntegerField(default=None)
    overview = models.TextField(default=None)
    genres = models.TextField(blank=True)
    cast = models.CharField(max_length=600, blank=True, null=True)
    crew = models.CharField(max_length=200, blank=True, null=True)
    production_companies = models.CharField(max_length=500 , blank=True , null = True)
    runtime = models.IntegerField( null = True , blank = True)
   
    

    def __str__(self):
        return self.title


    


    
class Theatre (models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=255)
    address = models.TextField()
    place = models.CharField(max_length=900)
    


    def __str__(self):
        return self.theatre_name
    

class Seat_Arrangement(models.Model):
    id = models.AutoField(primary_key=True, db_index=True , auto_created=True)
    no_seats = models.IntegerField()
    seat_arrangement = models.JSONField()## like {"premium" : 32 , "VIP" : 38 , "stand" : 40}
    no_rows = models.IntegerField()
    no_cols = models.IntegerField()
    

    def __str__(self):
        return f"{self.id}-rows{self.no_rows}-cols{self.no_cols}"
    

class MovieHall(models.Model):
    id = models.AutoField(primary_key=True, db_index=True , auto_created=True)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.IntegerField()
    seat_arrangement = models.ForeignKey(Seat_Arrangement , on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.theatre.name +"-"+ self.name +"-"+ self.id
    
class TheatreMovie(models.Model):
    id = models.AutoField(primary_key=True, db_index=True , auto_created=True)
    movie_hall = models.ForeignKey(MovieHall, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    release_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    
    
    def __str__(self):
        return self.movie_hall.name +"-"+ self.theatre.name +"-"+ self.movie.title +"-"+ self.start_time +"-"+ self.end_time +"-"+ self.date.strftime("%d-%m-%Y")

class Show (models.Model):
    id = models.AutoField(primary_key=True, db_index=True, auto_created=True)
    theatre_movie = models.ForeignKey(TheatreMovie, on_delete=models.CASCADE , null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.BooleanField(default=True)
    place = models.CharField(max_length=900)
    
    def __str__(self):
        return self.date +"-"+ self.theatre_movie


class SeatType(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    
    price = models.FloatField(null=True)
    def __str__(self):
        return self.name
    
class SeatId(models.Model):
    row = models.CharField(max_length=50 , null=True)
    number = models.CharField(max_length=50 , null= True)
    type = models.ManyToManyField(SeatType, verbose_name=("seat_type"), blank=True)
    def __str__(self):
        return f"Row: {self.row}, Number: {self.number}"


    
class Seat (models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    seat_id = models.ForeignKey(SeatId, on_delete=models.CASCADE , blank=True , null=True) 
     
    def __str__(self):
        return self.seat_id+"-"+ self.theatre.name
    
class Reservation (models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats = models.ManyToManyField(SeatType)
    theatre = models.ForeignKey(Theatre, on_delete=models.DO_NOTHING , default='')
    status = models.BooleanField(default=True)
    payment_id = models.CharField(max_length=255)

class Payment(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10 , decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
                                    