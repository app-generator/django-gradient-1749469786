# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Products(models.Model):

    #__Products_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Products_FIELDS__END

    class Meta:
        verbose_name        = _("Products")
        verbose_name_plural = _("Products")


class Customer(models.Model):

    #__Customer_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Customer_FIELDS__END

    class Meta:
        verbose_name        = _("Customer")
        verbose_name_plural = _("Customer")


class Customerhistory(models.Model):

    #__Customerhistory_FIELDS__
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)

    #__Customerhistory_FIELDS__END

    class Meta:
        verbose_name        = _("Customerhistory")
        verbose_name_plural = _("Customerhistory")



#__MODELS__END
