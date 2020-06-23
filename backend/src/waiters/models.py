from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=120, blank=False, unique=True)

    def __str__(self):
        return self.name


class Waiter(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120, blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                   related_name='waiters', blank=True, null=True)

    def __str__(self):
        return self.name
