from django.db import models
from datetime import datetime


class OurModel(models.Model):
    name = models.CharField(max_length=12, default='')
    fname = models.CharField(max_length=12, default='')
    phone = models.CharField(max_length=12, default='')
    date_of_birth = models.DateField(default=datetime.now)
    text = models.TextField(default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'our_model'
