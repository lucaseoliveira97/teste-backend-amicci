from django.db import models

from vendor.models import Vendor

class Retailer(models.Model):
    class Meta:

        db_table = 'retailer'

    name = models.CharField(max_length=200)
    vendors = models.ManyToManyField(Vendor, related_name="retailers", blank=True)

    def __str__(self):
        return self.name