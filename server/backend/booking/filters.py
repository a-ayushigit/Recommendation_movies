from django_filters import rest_framework as filters

from .models import Movies , Show , Reservation , Payment , Theatre , TheatreMovie

class TheatreMovieFilters(filters.FilterSet):
    title = filters.CharFilter(field_name="movie__title",lookup_expr="icontains")
    genre = filters.CharFilter(field_name="movie__genres",lookup_expr="icontains")
    cast = filters.CharFilter(field_name="movie__cast",lookup_expr="icontains")
    theatre = filters.CharFilter(field_name='theatre__name', lookup_expr='icontains')
    place = filters.CharFilter(field_name='theatre__place' , lookup_expr='icontains')
    # releasedate = filters.DateFilter(field_name="releasedate", lookup_expr="gte")

    class Meta:
        model = TheatreMovie
        fields = ['title' , 'genre' , 'cast' , 'theatre' , 'place']

class ShowFilters(filters.FilterSet):
    # theatre_movie = filters.CharFilter(field_name="theatre_movie")
    place = filters.CharFilter(field_name="place",lookup_expr="icontains")
    starttime = filters.TimeFilter(field_name="start_time", lookup_expr="gte")
    endtime = filters.TimeFilter(field_name="end_time", lookup_expr="lte")
    date = filters.DateFilter(field_name="date")

    class Meta:
        model = Show
        fields = ['theatre_movie', 'place', 'start_time', 'end_time' , 'date']

class TheatreFilters(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    place = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Theatre
        fields = ['name', 'place']