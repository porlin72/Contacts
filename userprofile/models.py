from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
     user = models.ForeignKey(User)
     
     def __unicode__(self):
        return "%s" % (self.user)