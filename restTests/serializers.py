from rest_framework import serializers
from .models import Address


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["name", "phone", "address", "created"]
