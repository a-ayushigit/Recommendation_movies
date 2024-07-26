from django.contrib import admin
from .models import Reservation , Payment , Theatre , Seat , Show
from recommendation.models import Movies
# Register your models here.
admin.site.register(Reservation )
 

admin.site.register(Payment )
admin.site.register(Theatre )
admin.site.register(Seat )
admin.site.register(Show )
admin.site.register(Movies )