from django.db import models


class Order(models.Model):
    custom_key = models.IntegerField(
        primary_key=True,
        serialize=False,
        default=-1)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    item = models.CharField(max_length=100)

    def __str__(self):
        return str(self.custom_key)
