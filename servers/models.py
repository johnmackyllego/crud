from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Server(models.Model):
    name = models.CharField(max_length=200,default = '')
    address = models.CharField(max_length=200,default = '')
    mobile = models.CharField(max_length=14,default = '')

    def __unicode__(self):
        return self.name
