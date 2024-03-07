from django.db import models

class Retailer(models.Model):
    class Meta:

        db_table = 'retailer'

    name = models.CharField(max_length=200)
    vendors = models.CharField(max_length=200)

    def __str__(self):
        return self.name