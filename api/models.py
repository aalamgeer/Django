# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)


'''class city(models.Model):
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    city_hall = models.CharField(max_length=50)'''


class employee(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    empCode = models.CharField(max_length=50)

    def __str__(self):
        return self.fname

