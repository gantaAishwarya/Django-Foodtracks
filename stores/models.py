from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

#Telling django that this is a Model class
class Store(models.Model):
    # Using ID as Universal Unique Identifier
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    #company_id = 
    name = models.CharField(max_length=200,null=False, help_text=_("Name of the bakery"))
    address = models.CharField(null=True, blank=True, max_length=500, help_text=_("Address of the bakery"))
    is_open = models.BooleanField(default=True, help_text=_("Whether the store is currently open"))

    class Meta:
        #When quering order by descending order of alphabets
        ordering = ["-name"]

    def __str__(self):
        return self.name + ' ' + self.address

class StoreHours(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Day of week should be between 1 and 7."),
            MaxValueValidator(7, message="Day of week should be between 1 and 7.")
        ]
    )
    opens = models.TimeField()
    closes = models.TimeField()
    #valid_from = models.DateTimeField()
    #valid_through = models.DateTimeField()

        

