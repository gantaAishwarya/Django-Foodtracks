from django.contrib import admin
from .models import Store, StoreHours

#show models in django admin panel
class StoreAdmin(admin.ModelAdmin):
    search_fields = ["name", "address"]
    list_display = ["name", "address"]

admin.site.register(Store)
admin.site.register(StoreHours)