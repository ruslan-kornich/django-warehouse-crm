from django.db import models


class VolunteerOrganization(models.Model):
    name = models.CharField(max_length=200)


class Warehouse(models.Model):
    organization = models.OneToOneField(VolunteerOrganization, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Shipment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)


class Distribution(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)
