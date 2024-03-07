from django.db import models
from retailer.models import Retailer
class Vendor(models.Model):
    class Meta:

        db_table = 'vendor'

    name = models.CharField(max_length=200)
    retailer = models.ForeignKey(Retailer, related_name="vendors", on_delete=models.CASCADE)

    def __str__(self):
        return self.name