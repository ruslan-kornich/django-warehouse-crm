from rest_framework import serializers
from .models import (
    VolunteerOrganization,
    Warehouse,
    Product,
    Inventory,
    Shipment,
    Distribution,
)


class VolunteerOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerOrganization
        fields = "__all__"


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = "__all__"


class DistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribution
        fields = "__all__"
