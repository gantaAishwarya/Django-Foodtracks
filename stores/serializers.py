from rest_framework import serializers
from .models import Store, StoreHours

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"
        #fields = ['id', 'name', 'address']
        read_only_fields = ["id"]


class StoreHoursSerializer(serializers.ModelSerializer):
    def validate(self, data):
        opens = data.get("opens")
        closes = data.get("closes")

        if opens and closes:
            if opens >= closes:
                raise serializers.ValidationError("Opening time must be before closing time.")

        return data
    class Meta:
        model = StoreHours
        fields = "__all__"
        read_only_fields = ["id"]

