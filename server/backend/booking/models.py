from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime , timedelta 

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
        return self.name
    



class Seat_Arrangement(models.Model):
    id = models.AutoField(primary_key=True, db_index=True , auto_created=True)
    no_seats = models.IntegerField()
    seat_arrangement = models.JSONField()## like {"premium" : 32 , "VIP" : 38 , "stand" : 40}
    no_rows = models.IntegerField()
    no_cols = models.IntegerField()
    

    def __str__(self):
        return f"{self.id}-rows{self.no_rows}-cols{self.no_cols}"
    

class MovieHall(models.Model):
    id = models.CharField(primary_key=True, db_index=True )
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.IntegerField()
    seat_arrangement = models.ForeignKey(Seat_Arrangement , on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.theatre.name +"-"+ self.name +"-"+ self.id
    
class TheatreMovie(models.Model):
    id = models.CharField(primary_key=True, db_index=True , auto_created=True)
    movie_hall = models.ForeignKey(MovieHall, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    release_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    
    
    def __str__(self):
        return self.movie_hall.name +"-"+ self.theatre.name +"-"+ self.movie.title  +"-"+ self.release_date.strftime("%d-%m-%Y")

class Show (models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    theatre_movie = models.ForeignKey(TheatreMovie, on_delete=models.CASCADE , null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.BooleanField(default=True)
    place = models.CharField(max_length=900)
    
    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} +'-'+ {self.theatre_movie}"


class SeatType(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    
    price = models.FloatField(null=True)
    def __str__(self):
        return self.name
    
class SeatId(models.Model):
    
    number = models.CharField(max_length=50 , null= True)
    type = models.ForeignKey(SeatType, blank=True , on_delete=models.CASCADE , default=None)
    
    def __str__(self):
        return f"Row: {self.row}, Number: {self.number}"


    
class Seat (models.Model):
    id = models.AutoField(primary_key=True, db_index=True, default=None)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    seat_id = models.JSONField(default = dict)
    movie_hall = models.ForeignKey(MovieHall, on_delete=models.CASCADE, null = True , blank=True)
    seat_arrangement = models.ForeignKey(Seat_Arrangement, on_delete=models.CASCADE , null = True , blank=True)
    status = models.BooleanField(default=False)#whether the seat is booked - true , else false
     
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
                                    

class RecurrenceModel(models.Model):
    DAILY='daily'
    WEEKLY='weekly'
    MONTHLY='monthly'

    #define the tuples 
    recurrence_choices = [
        (DAILY , 'daily'),
        (WEEKLY , 'weekly'),
        (MONTHLY, 'monthly')
    ]

    #define the model 
    theatre_movie=models.ForeignKey(TheatreMovie , on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    recurrence_type = models.CharField(max_length=7 , choices = recurrence_choices , default = DAILY)
    interval= models.IntegerField(default=1)#define the no. of days between 
    start_time = models.TimeField()
    end_time = models.TimeField()

    def generate_occurrences(self):
        occurrences = []
        current_date = self.start_date
        # print("Hello I entered")
        while current_date <= self.end_date:
            # print("Hello I entered while loop")
            try :
                if self.is_conflict(current_date , self.start_time , self.end_time):
                    # print("Hello I entered validation error")
                    raise ValidationError(f"Time conflict detected for this show {self.theatre_movie.movie.title} at {self.theatre_movie.movie_hall.name} on {current_date}")
                    
            except ValidationError as e:
                print(e)
                if self.recurrence_type == self.DAILY :
                    current_date += timedelta(days=self.interval)
                elif self.recurrence_type == self.WEEKLY:
                    current_date += timedelta(weeks = self.interval)
                elif self.recurrence_type == self.MONTHLY:
                    current_date = self.add_months(current_date , self.interval)
                # print("Hello I am printing error and i should continue")
                continue
            
            occurrences.append(Show.objects.create(
                theatre_movie = self.theatre_movie,
                date=current_date,
                start_time=self.start_time,
                end_time=self.end_time,
                status=True,
                place=self.theatre_movie.theatre.place


            ))
            # print("Hello I entered and appended the occurrences list")
            if self.recurrence_type == self.DAILY :
                current_date += timedelta(days=self.interval)
            elif self.recurrence_type == self.WEEKLY:
                current_date += timedelta(days = self.interval)
            elif self.recurrence_type == self.MONTHLY:
                current_date = self.add_months(current_date , self.interval)
            # print("Hello I entered and added the recurrence number of days , months , years ")
        return occurrences
    
    def is_conflict(self , date , start_time , end_time):
        conflicting_shows = Show.objects.filter(
            ##double underscore used to traverse foreign key queries 
            theatre_movie__movie_hall = self.theatre_movie.movie_hall,
            date=date,
            start_time__lt = end_time,
            end_time__gt = start_time


        )
        # print("Hello I entered and i am returning conflict")
        return conflicting_shows.exists()
    
    def add_months(self, date, months):
        month = date.month  + months
        year = date.year + month // 12
        month = month % 12 
        day = min(date.day, [31,
            29 if ((year % 4 == 0) and (not year % 100 == 0)) or (year % 400 == 0) else 28,
            31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month-1])
        # print("Hello I entered and added month")
        return date.replace(year=year, month=month, day=day)

            