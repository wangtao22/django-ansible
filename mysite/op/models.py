from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

class Resources(models.Model):
    name = models.CharField(max_length=20)
    ip = models.GenericIPAddressField(unique=True)
    c_time = models.DateTimeField(default=timezone.now)
    


    class Meta:
        ordering = ("-c_time",)
    
    def __str__(self):
        return self.name

