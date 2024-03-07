from django.db import models

class Briefing(models.Model):
    class Meta:

        db_table = 'briefing'

    name = models.CharField(max_length=200)
    retailer = models.CharField(max_length=200)
    responsible = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)
    availabe = models.IntegerField()

    def __str__(self):
        return self.name