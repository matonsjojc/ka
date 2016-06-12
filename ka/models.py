from django.contrib.auth.models import User
from django.db import models

class Pacient(models.Model):
    user = models.OneToOneField(User, null=True)
    ime = models.CharField(max_length=120, null=True) #zamenjaj z userjem
    ponudnik = models.ForeignKey('Ponudnik', null=True)
    #dodaj še id, odgovore
    def __str__(self):
        return self.ime#self.user.username

class Aparat(models.Model):
    proizvajalec = models.CharField(max_length=120) #zamenjaj s choices...
    vrsta_terapije = models.CharField(max_length=120, null=True)
    pacient = models.ForeignKey('Pacient', null=True)
    #dodaj še: model, nastavitev,
    def __str__(self):
        return self.proizvajalec
"""

class Maska(models.Model):
    tip = models.CharField(max_length=120)
    pacient = models.ForeignKey('Pacient', null=True)

    def __str__(self):
        return self.tip
"""

class Ponudnik(models.Model):
    ime = models.CharField(max_length=120)

    def __str__(self):
        return self.ime

#dodaj modela vprasanje, odgovor
