# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Email = models.EmailField()
    PhoneNumber = models.BigIntegerField()
    Address = models.CharField(max_length=200)
    CV = models.FileField()

    def __str__(self):
        return self.FirstName