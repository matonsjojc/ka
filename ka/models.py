from django.contrib.auth.models import User
from django.db import models

#modeli v zvezi s terapijo:
class Pacient(models.Model):
    user = models.OneToOneField(User, null=True)
    ime = models.CharField(max_length=120, null=True) #ta info daj v userja
    ponudnik = models.ForeignKey('Ponudnik', null=True)
    #dodaj se id, meta: verbose_name_plural

    def __str__(self):
        return self.ime#self.user.username

class Aparat(models.Model):
    proizvajalec = models.CharField(max_length=250) #zamenjaj s choices...
    pacient = models.ForeignKey('Pacient', null=True)
    #dodaj še: model
    def __str__(self):
        return self.proizvajalec

class Maska(models.Model):
    name = models.CharField(max_length=250)
    pacient = models.ForeignKey('Pacient', null=True)

    def __str__(self):
        return self.name

class Ponudnik(models.Model):
    ime = models.CharField(max_length=120)

    def __str__(self):
        return self.ime

class Nastavitve(models.Model):
    pass

# ----- modeli v zvezi z vprasalnikom: -----
class Vprasanje(models.Model): #ta model naredi neizbrisljiv v adminu?
    tekst = models.CharField(max_length=250)
    komentar_k_tekstu = models.TextField(blank=True, null=True)
    #datum_objave = models.DateTimeField('datum objave', blank=True) #naredi prepopulated
    aktiven = models.BooleanField(default=True)
    #datum_spremembe?

    def __str__(self):
        return self.tekst

class Odgovor(models.Model):
    vprasanje = models.ForeignKey(Vprasanje, null=True)
    tekst = models.CharField(max_length=250, null=True)
    #komentar_k_tekstu = models.TextField(blank=True)
    #datum_objave = models.DateTimeField('datum objave', blank=True) #naredi prepopulated

    def __str__(self):
        return self.tekst

class Anketa(models.Model):
    # seznam aktivnih vprasanj in odgovorov
    #datum_izpolnjevanja = models.DateTimeField('datum izpolnjevanja', blank=True)

    def seznam_vprasanj(self):
        vprasanja = Vprasanje.objects.all().filter(aktiven=True) #verjetno bo treba order_by, da bodo obrnjena,
        #da jih popaš... l8r.
        return vprasanja

    def seznam_odgovorov(self):
        odgovori = Odgovor.objects.all()
        return odgovori
