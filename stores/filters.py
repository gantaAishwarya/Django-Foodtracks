from django_filters import rest_framework as filters
from .models import StoreHours

class StoreHoursFilter(filters.FilterSet):
    day_of_week = filters.NumberFilter(field_name='day_of_week')

    class Meta:
        model = StoreHours
        fields = ['day_of_week',] 
