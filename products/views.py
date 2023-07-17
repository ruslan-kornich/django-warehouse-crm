from rest_framework import viewsets
from .models import (
    VolunteerOrganization,
    Warehouse,
    Product,
    Inventory,
    Shipment,
    Distribution,
)
from .serializers import (
    VolunteerOrganizationSerializer,
    WarehouseSerializer,
    ProductSerializer,
    InventorySerializer,
    ShipmentSerializer,
    DistributionSerializer,
)


class VolunteerOrganizationViewSet(viewsets.ModelViewSet):
    queryset = VolunteerOrganization.objects.all()
    serializer_class = VolunteerOrganizationSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer


class DistributionViewSet(viewsets.ModelViewSet):
    queryset = Distribution.objects.all()
    serializer_class = DistributionSerializer
