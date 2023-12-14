from django_filters import rest_framework as filters
from .models import StoreHours, Store

class StoreFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name')

    class Meta:
        model = Store
        fields = ['name']


class StoreHoursFilter(filters.FilterSet):
    day_of_week = filters.NumberFilter(field_name='day_of_week')

    class Meta:
        model = StoreHours
        fields = ['day_of_week',] 
