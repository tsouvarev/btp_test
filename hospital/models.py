# coding=utf-8

from django.db import models


class Speciality(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    speciality = models.ForeignKey(Speciality, related_name="doctors")

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.speciality.name)


class Patient(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Ticket(models.Model):
    doctor = models.ForeignKey(Doctor, related_name="tickets")
    date_time = models.DateTimeField()
    patient = models.ForeignKey(Patient, related_name="tickets", null=True)

    def __unicode__(self):
        return u"%s to %s at %s" % (self.patient.name if self.patient else u"No one", self.doctor, self.date_time)