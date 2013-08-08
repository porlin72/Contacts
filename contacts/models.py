from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    number = models.CharField(max_length=20, blank=True, null=True)
    
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)