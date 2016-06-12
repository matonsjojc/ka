from django.contrib.auth.models import User
from django.db import models

class Pacient(models.Model):
    user = models.OneToOneField(User, null=True)
    ime = models.CharField(max_length=120, null=True) #ta info daj v userja
    ponudnik = models.ForeignKey('Ponudnik', null=True)
    #dodaj še id, odgovore, meta: verbose_name_plural

    def __str__(self):
        return self.ime#self.user.username

class Aparat(models.Model):
    proizvajalec = models.CharField(max_length=120) #zamenjaj s choices...
    pacient = models.ForeignKey('Pacient', null=True)
    #vrsta_terapije = models.CharField(max_length=120, null=True)
    #dodaj še: model, nastavitev,
    def __str__(self):
        return self.proizvajalec

class Maska(models.Model):
    name = models.CharField(max_length=120)
    pacient = models.ForeignKey('Pacient', null=True)

    def __str__(self):
        return self.name

class Ponudnik(models.Model):
    ime = models.CharField(max_length=120)

    def __str__(self):
        return self.ime

#dodaj modela vprasanje, odgovor
