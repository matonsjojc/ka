import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'kontrole_project.settings')

import django
django.setup()
from django.contrib.auth.models import User
from ka.models import Pacient, Ponudnik, Aparat#, Maska

def populate():

    userji = [
        {"username": "prvi_pacient", "password": "geslozatest", "email": "test@testni_mail.com"},
        {"username": "drugi_pacient", "password": "geslozatest", "email": "test@testni_mail.com"},
        {"username": "tretji_pacient", "password": "geslozatest", "email": "test@testni_mail.com"},
    ]

    pacienti = [
        {"user": "prvi_pacient", "ime": "Anja Ažman", "aparat": "Philips", "ponudnik": "Pulmodata"}, #"maska": "Philips Respironics Comfortgel"
        {"user": "drugi_pacient", "ime": "Bojan Bogdanović", "aparat": "Devilbiss", "ponudnik": "Medicotehna"}, #"maska": "Resmed Mirage Quattro"
        {"user": "tretji_pacient", "ime": "Cene Cakuta", "aparat": "Fisher & Paykel", "ponudnik": "Medicotehna"}, #"maska": "Weinmann JoyceEasy",
        ]

    aparati = [
    """
        {"proizvajalec": "Philips"},
        {"proizvajalec": "Devilbiss"},
        {"proizvajalec": "Fisher & Paykel"},
        ]
    """

    ponudniki = [
        {"ime": "Pulmodata"},
        {"ime": "Medicotehna"},
        {"ime": "Sapio"},
        ]

    for us in userji:
        dodaj_userja(us["username"], us["email"], us["password"])
    for pon in ponudniki:
        dodaj_ponudnika(pon["ime"])
    for pac in pacienti:
        dodaj_pacienta(pac["user"], pac["ime"], pac["aparat"], pac["ponudnik"])
    for apa in aparati:
        dodaj_aparat(ap["proizvajalec"])

def dodaj_userja(username, email, password):
    u = User.objects.get_or_create(username=username, email=email, password=password)[0]
    print(u)

def dodaj_pacienta(user, ime, aparat, ponudnik):#, maska, ponudnik):
    p = Pacient.objects.get_or_create(ime=ime)[0]
    pon = Ponudnik.objects.get(ime=ponudnik)
    p.ponudnik=pon
    usr = User.objects.get(username=user)
    p.user = usr
    p.save()
    print(p)
    return p

def dodaj_ponudnika(ime):
    p = Ponudnik.objects.get_or_create(ime=ime)[0]
    p.ime = ime
    p.save()
    print(p)
    return p

def dodaj_aparate():
   # tole spodaj je narobe; pojdi skozi seznam pacientov in za vsakega ustvari instanco Aparata,
   # kot proizvajalca napišeš tisto, kar pač ima :)

    a = Aparat.objects.get_or_create(proizvajalec=proizvajalec)
    pac = Pacient.objects.get(id = pacient.id)
    a.pac = pac
    a.save()
    print("dodajam aparat:", a)
    return a

if __name__ == '__main__':
    print("Starting population script...")
    populate()
