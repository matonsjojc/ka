import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'kontrole_project.settings')

import django
django.setup()
from ka.models import Pacient #, Maska, Aparat, Ponudnik

def populate():

    pacienti = [
        {"ime": "Anja Ažman", "aparat": "Philips"}, #"maska": "Philips Respironics Comfortgel", "ponudnik": "Pulmodata"},
        {"ime": "Bojan Bogdanović", "aparat": "Devilbiss"}, #"maska": "Resmed Mirage Quattro" , "ponudnik": "Medicotehna"},
        {"ime": "Cene Cakuta", "aparat": "Fisher & Paykel"}, #"maska": "Weinmann JoyceEasy" , "ponudnik": "Medicotehna"},
        ]

    """
    aparati = [
        {"proizvajalec": "Philips"},
        {"proizvajalec": "Devilbiss"},
        {"proizvajalec": "Fisher & Paykel"},
        ]
    """
    for pac in pacienti:
        dodaj_pacienta(pac["ime"], pac["aparat"])


def dodaj_pacienta(ime, aparat):#, maska, ponudnik):
    p = Pacient.objects.create()
    #(ime=ime, aparat=aparat, maska=maska, ponudnik=ponudnik)
    p.ime = ime
    p.aparat = aparat
    #p.maska = maska
    #p.ponudnik = ponudnik
    p.save()
    print(p)
    return p

if __name__ == '__main__':
    print("Starting population script...")
    populate()
