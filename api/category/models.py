from django.db import models

class Category(models.Model):
    class Meta:

        db_table = 'category'

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name