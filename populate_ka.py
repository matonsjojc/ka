import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'kontrole_project.settings')

import django
django.setup()
from django.contrib.auth.models import User
from ka.models import Pacient, Ponudnik, Aparat, Maska

def populate():

    userji = [
        {"username": "prvi_pacient", "password": "geslozatest", "email": "test@testni_mail.com"},
        {"username": "drugi_pacient", "password": "geslozatest", "email": "test@testni_mail.com"},
        {"username": "tretji_pacient", "password": "geslozatest", "email": "test@testni_mail.com"},
    ]

    pacienti = [
        {
         "user": "prvi_pacient",
         "ime": "Anja Ažman",
         "aparat": "Philips",
         "ponudnik": "Pulmodata",
         "maska": "Philips Respironics Comfortgel",
         },
        {
         "user": "drugi_pacient",
         "ime": "Bojan Bogdanović",
         "aparat": "Devilbiss",
         "ponudnik": "Medicotehna",
         "maska": "Resmed Mirage Quattro",
         },
        {
         "user": "tretji_pacient",
         "ime": "Cene Cakuta",
         "aparat": "Fisher & Paykel",
         "ponudnik": "Medicotehna",
         "maska": "Weinmann JoyceEasy",
         },
        ]

    ponudniki = [
        {"ime": "Pulmodata"},
        {"ime": "Medicotehna"},
        {"ime": "Sapio"},
        ]

    #ustvari userje:
    for us in userji:
        dodaj_userja(us["username"], us["email"], us["password"])
    #ustvari ponudnike:
    for pon in ponudniki:
        dodaj_ponudnika(pon["ime"])
    #ustvari paciente, jih poveže s ponudnikom; za vsakega pacienta ustvari aparat, masko in tega poveže s pacientom:
    for pac in pacienti:
        p = dodaj_pacienta(pac["user"], pac["ime"], pac["ponudnik"])
        dodaj_aparat_in_masko(p, pac["aparat"], pac["maska"])

def dodaj_userja(username, email, password):
    u = User.objects.get_or_create(username=username, email=email, password=password)[0]
    print("Dodajam userja: ", u)

def dodaj_pacienta(user, ime, ponudnik):
    p = Pacient.objects.get_or_create(ime=ime)[0]
    pon = Ponudnik.objects.get(ime=ponudnik)
    p.ponudnik=pon
    usr = User.objects.get(username=user)
    p.user = usr
    p.save()
    print("Dodajam pacienta: ", p)
    return p

def dodaj_ponudnika(ime):
    p = Ponudnik.objects.get_or_create(ime=ime)[0]
    p.ime = ime
    p.save()
    print("Dodajam ponudnika: ", p)
    return p

#ustvari aparat in masko ter ju doda k obstojecemu pacientu, arg: Pacient, proizvajalec, maska
def dodaj_aparat_in_masko(pacient, aparat, maska):
    a = Aparat.objects.get_or_create(proizvajalec=aparat)[0]
    m = Maska.objects.get_or_create(name=maska)[0]
    pac = Pacient.objects.get(id=pacient.id)
    a.pacient = pac
    m.pacient = pac
    a.save()
    m.save()
    print("Dodajam aparat: ", a, " --- Dodajam masko:", m)
    return a

if __name__ == '__main__':
    print("Starting population script...")
    populate()
