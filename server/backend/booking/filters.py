from django_filters import rest_framework as filters

from .models import Movies , Show , Reservation , Payment , Theatre

class MovieFilters(filters.FilterSet):
    title = filters.CharFilter(field_name="title",lookup_expr="icontains")
    genre = filters.CharFilter(field_name="genres",lookup_expr="icontains")
    cast = filters.CharFilter(field_name="cast",lookup_expr="icontains")
    # releasedate = filters.DateFilter(field_name="releasedate", lookup_expr="gte")

    class Meta:
        model = Movies
        fields = ['title' , 'genre' , 'cast' ]

class ShowFilters(filters.FilterSet):
    movie = filters.CharFilter(lookup_expr="iexact")
    theatre = filters.CharFilter(lookup_expr="iexact")
    starttime = filters.TimeFilter(field_name="start_time", lookup_expr="gte")
    endtime = filters.TimeFilter(field_name="end_time", lookup_expr="lte")
    date = filters.DateFilter(field_name="date",lookup_expr="iexact")

    class Meta:
        model = Show
        fields = ['movie', 'theatre', 'start_time', 'end_time' , 'date']

class TheatreFilters(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    place = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Theatre
        fields = ['name', 'place']