from rest_framework import serializers
from .models import Store, StoreHours

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        #instructs the serializer to include all fields
        fields = "__all__"
        #fields = ['id', 'name', 'address']
        #id field should be treated as read-only during serialization/deserialization
        read_only_fields = ["id"]


class StoreHoursSerializer(serializers.ModelSerializer):
    #Validation on open and close hours
    def validate(self, data):
        opens = data.get("opens")
        closes = data.get("closes")

        if opens and closes:
            if opens >= closes:
                raise serializers.ValidationError("Opening time must be before closing time.")

        return data
    class Meta:
        model = StoreHours
        #instructs the serializer to include all fields
        fields = "__all__"
        #id field should be treated as read-only during serialization/deserialization
        read_only_fields = ["id"]

