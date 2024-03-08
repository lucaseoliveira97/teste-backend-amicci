from django.db import models
from retailer.models import Retailer

from category.models import Category

class Briefing(models.Model):
    class Meta:

        db_table = 'briefing'

    name = models.CharField(max_length=200)
    retailer = models.ForeignKey(Retailer, related_name="retailer", on_delete=models.CASCADE)
    responsible = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    release_date = models.CharField(max_length=200)
    availabe = models.IntegerField()

    def __str__(self):
        return self.name