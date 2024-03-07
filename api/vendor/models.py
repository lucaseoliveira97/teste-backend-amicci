from django.db import models

class Vendor(models.Model):
    class Meta:

        db_table = 'vendor'

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name