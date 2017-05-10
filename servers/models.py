from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator

# Create your models here.
class Server(models.Model):
    name = models.CharField(max_length=200,default = '')
    address = models.CharField(max_length=200,default = '')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile = models.CharField(validators=[phone_regex], blank=True,max_length = 13) # validators should be a list

    def __unicode__(self):
        return self.name
