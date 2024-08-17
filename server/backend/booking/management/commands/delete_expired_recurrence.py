import random 
from datetime import datetime , timedelta 
from django.core.management.base import BaseCommand 
from booking.models import RecurrenceModel ,TheatreMovie , Show

class Command(BaseCommand):
    help="Delete expired recurrences "
    def handle(self , *args , **kwargs):
        today = datetime.now().date()
        expired_recurrences = RecurrenceModel.objects.filter(
            end_date__lt = today
        )
        count , _ = expired_recurrences.delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} expired Recurrence instances'))