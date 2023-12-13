import factory
from factory import Faker
from stores.models import Store, StoreHours

class StoreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Store
    
    name = Faker('company')
    address = Faker('address')

class StoreHoursFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StoreHours
    
    store_id = factory.SubFactory(StoreFactory)
    day_of_week = Faker('pyint', min_value=1, max_value=7) 
    opens = Faker('time', pattern='%H:%M:%S')  
    closes = Faker('time', pattern='%H:%M:%S') 
    #valid_from = Faker('date_time_this_year', before_now=True, after_now=False)
    #valid_through = Faker('date_time_between', start_date='+1y', end_date='+5y')
