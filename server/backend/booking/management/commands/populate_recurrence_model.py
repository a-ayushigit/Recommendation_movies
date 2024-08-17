import random 
from datetime import datetime , timedelta 
from django.core.management.base import BaseCommand 
from booking.models import RecurrenceModel ,TheatreMovie , Show
from django.db import connection
class Command(BaseCommand):
    help="Populate the recurrence model with dummy data "
    
    def handle(self , *args , **kwargs):
        # count = 0
        with connection.cursor() as cursor:
            # print("hello")
            # cursor.execute("TRUNCATE TABLE booking_show RESTART IDENTITY CASCADE;")
            cursor.execute("SELECT setval(pg_get_serial_sequence('booking_show' , 'id'),1,false);")
        
        # count += 1
        # print(f"hello {count}")
        # print("passed connection ")
        theatre_movies = TheatreMovie.objects.all()
        recurrence_types= [RecurrenceModel.DAILY , RecurrenceModel.WEEKLY , RecurrenceModel.MONTHLY]
        for theatre_movie in theatre_movies:
            start_date = theatre_movie.release_date
            end_date = theatre_movie.end_date
            recurrence_type = random.choice(recurrence_types)
            interval = random.randint(1,3)
            # count += 1
            # print(f"hello {count}")
            # print("entered theatre movie for loop")
            for i in range(5):
                start_hour = random.randint(0,23)
                start_minute = random.randint(0,59)
                start_time = datetime.time(datetime(year=2000 , month=1 , day=1 , hour=start_hour , minute = start_minute))
                runtime_hours = theatre_movie.movie.runtime // 60
                runtime_minutes = theatre_movie.movie.runtime % 60
                end_time = (datetime.combine(datetime.today(), start_time) + timedelta(hours=runtime_hours , minutes= runtime_minutes)).time()
                # count += 1
                # print(f"hello {count}")
                # print("entered 5 range for loop")
                # existing_shows = Show.objects.filter(
                #     theatre_movie__movie_hall = theatre_movie.movie_hall,
                #     start_time__lte=end_time,
                #     end_time__gte = start_time,
                #     date = start_date,
                #     date = end_date

                # )
                # if not existing_shows.exists():
                recurrence = RecurrenceModel.objects.create(
                        theatre_movie=theatre_movie,
                        start_date=start_date,
                        end_date=end_date,
                        recurrence_type=recurrence_type,
                        interval=interval,
                        start_time=start_time,
                        end_time=end_time
                    )
                # print(recurrence)
                # count += 1
                # print(f"hello {count}")
                # print("created recurrence")
                occurrences = recurrence.generate_occurrences()
                # for occurrence in occurrences:
                #     print(occurrence)
                # print(occurrences)
                # Show.objects.bulk_create(occurrences)
                # count += 1
                # print(f"hello {count}")
                # print("created show instance ")
        self.stdout.write(self.style.SUCCESS('Successfully populated the recurrence and show database '))
     
       