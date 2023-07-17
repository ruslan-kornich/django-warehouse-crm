from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    VolunteerOrganizationViewSet,
    WarehouseViewSet,
    ProductViewSet,
    InventoryViewSet,
    ShipmentViewSet,
    DistributionViewSet,
)

router = DefaultRouter()
router.register(r"organizations", VolunteerOrganizationViewSet)
router.register(r"warehouses", WarehouseViewSet)
router.register(r"products", ProductViewSet)
router.register(r"inventories", InventoryViewSet)
router.register(r"shipments", ShipmentViewSet)
router.register(r"distributions", DistributionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
