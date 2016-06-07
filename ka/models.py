from django.contrib.auth.models import User
from django.db import models

class Pacient(models.Model):
    user = models.OneToOneField(User)
    aparat = models.OneToOneField('Aparat')
    maska = models.OneToOneField('Maska')
    ponudnik = models.ForeignKey('Ponudnik')
    #dodaj še id, odgovore
    def __str__(self):
        return self.user.username

class Aparat(models.Model):
    proizvajalec = models.CharField(max_length=120)
    vrsta_terapije = models.CharField(max_length=120)
    ponudnik = models.ForeignKey('Ponudnik')
    #dodaj še: model, nastavitev,
    def __str__(self):
        return self.proizvajalec

class Maska(models.Model):
    tip = models.CharField(max_length=120)

    def __str__(self):
        return self.tip

class Ponudnik(models.Model):
    ime = models.CharField(max_length=120)

    def __str__(self):
        return self.ime

#dodaj modela vprasanje, odgovor
