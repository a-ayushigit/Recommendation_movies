from django_filters import rest_framework as filters
from recommendation.models import Movies
from .models import Show , Reservation , Payment , Theatre , Seat 

class MovieFilters(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="icontains")
    genre = filters.CharFilter(lookup_expr="icontains")
    actors = filters.CharFilter(lookup_expr="icontains")
    release_date = filters.DateFilter(field_name="release_date", lookup_expr="gte")

    class Meta:
        model = Movies
        fields = ['title' , 'genre' , 'cast' , 'release_date']

class ShowFilters(filters.FilterSet):
    movie = filters.CharFilter('movie')
    theatre = filters.CharFilter('theatre')
    date = filters.DateFilter('date')
    time = filters.DateFilter('time')

    class Meta:
        model = Show
        fields=['movie' , 'theatre' , 'date' , 'time']

class TheatreFilters(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    place = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Theatre
        fields=['name' , 'place']
