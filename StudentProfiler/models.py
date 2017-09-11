from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Faculty(User):
    #firstName=models.CharField(max_length=264)
    #lastName=models.CharField(max_length=264)
    pass

class Students(models.Model):
    UID=models.CharField(max_length=14)
    subject=models.CharField(max_length=10)
    category=models.CharField(max_length=10)

    def __str__(self):
        return str(self.UID)
    def __unicode__(self):
        return u'%s %s %s' % (self.UID, self.subject, self.category)

class Marks(models.Model):
    uid=models.CharField(max_length=10)
    subject=models.CharField(max_length=10)
    ut1=models.IntegerField(validators=[MaxValueValidator(20), MinValueValidator(0)])
    ut2=models.IntegerField(validators=[MaxValueValidator(20), MinValueValidator(0)])
    sem=models.IntegerField(validators=[MaxValueValidator(80), MinValueValidator(0)])
    total=models.IntegerField(validators=[MaxValueValidator(200), MinValueValidator(0)])

    def __str__(self):
        return str(self.total)
