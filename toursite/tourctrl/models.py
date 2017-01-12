from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Touruser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uico = models.CharField(max_length=255, null=True)
    usign = models.CharField(max_length=31, blank=True, null=True)
    ulocation = models.CharField(max_length=63, blank=True, null=True)
    ujointime = models.CharField(max_length=15)
    utag = models.CharField(max_length=255, blank=True, null=True)


class Tourdest(models.Model):
    did = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=63)
    dinfo = models.CharField(max_length=255)
    drealweather = models.TextField(blank=True, null=True)



class Tourjournal(models.Model):
    jid = models.AutoField(primary_key=True)
    jcover = models.CharField(max_length=255, blank=True, null=True)
    jname = models.CharField(max_length=63)
    jdescrip = models.CharField(max_length=255)
    jcontent = models.TextField()
    juser = models.ForeignKey(Touruser, on_delete=models.DO_NOTHING)
    jtag = models.CharField(max_length=255, blank=True, null=True)



class Tourspot(models.Model):
    sid = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=63)
    scover = models.CharField(max_length=255)
    sinfo = models.TextField()
    sdest = models.ForeignKey(Tourdest, models.DO_NOTHING)



class Tourtrip(models.Model):
    tid = models.AutoField(primary_key=True)
    tcover = models.CharField(max_length=255)
    tname = models.CharField(max_length=63)
    tdescrip = models.CharField(max_length=255)
    tdays = models.IntegerField()
    tpeople = models.CharField(max_length=63)
    ttrip = models.TextField()
    tdest = models.ForeignKey(Tourdest, models.DO_NOTHING)
    tspot = models.ForeignKey(Tourspot, models.DO_NOTHING)
