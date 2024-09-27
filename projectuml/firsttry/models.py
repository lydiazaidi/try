from cmath import cos, sin, sqrt
from datetime import timedelta, timezone
from math import atan2, radians
from typing import Self

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class Ville(models.Model):
    idville = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)


class Trajet(models.Model):
    idtrajet = models.IntegerField(primary_key=True)
    villeD = models.ForeignKey(Ville, related_name='trajets_departure', on_delete=models.CASCADE)
    villeA = models.ForeignKey(Ville, related_name='trajets_arrival', on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=15, decimal_places=2)
    distance=models.DecimalField(max_digits=10, decimal_places=2)
    duree = models.DurationField()
     
    def calculer_prix_et_duree(self):
        # Calculer la distance entre les villes en utilisant la latitude et la longitude
        lat1 = float(self.villeD.latitude)
        lon1 = float(self.villeD.longitude)
        lat2 = float(self.villeA.latitude)
        lon2 = float(self.villeA.longitude)
        distance_km = self.calculer_distance(lat1, lon1, lat2, lon2)
       


        # Calculer le prix en fonction de la distance (ex: prix par kilomètre)
        prix_par_km = 0.1  # Prix par kilomètre (exemple)
        prix = distance_km * prix_par_km
        distance=distance_km


        # Calculer la durée en fonction de la distance (ex: vitesse moyenne)
        vitesse_moyenne = 800  # Vitesse moyenne en kilomètres par heure (exemple)
        temps_heures = distance_km / vitesse_moyenne
        duree = timedelta(hours=temps_heures)


        # Mettre à jour les champs prix et durée du trajet
        self.prix = prix
        self.duree = duree
        self.distance=distance
        self.save()


    @staticmethod
    def calculer_distance(lat1, lon1, lat2, lon2):
        print(f"lat1: {lat1}, lon1: {lon1}, lat2: {lat2}, lon2: {lon2}")
        # Convertir les degrés en radians
        lat1_rad, lon1_rad = radians(lat1), radians(lon1)
        lat2_rad, lon2_rad = radians(lat2), radians(lon2)
       
        # Calcul des différences de latitude et de longitude
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
       
        # Formule de la distance haversine
        a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(max(0.0, a.real)), sqrt(max(0.0, (1.0 - a).real)))
        distance_km = 6371 * c.real  # Use the real part of the complex number
       
        return distance_km



class Vol(models.Model):
    num_vol = models.IntegerField(primary_key=True)
    dateD = models.DateField(default=timezone.now)
    timeD = models.TimeField(default=timezone.now)
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)
    img=models.ImageField(default='images/default-image.jpg')


class Reservation(models.Model):
    id_reservation = models.IntegerField(primary_key=True)
    date = models.DateField()
    heur = models.TimeField()
    nbr_places = models.IntegerField()
    vol = models.ForeignKey(Vol, on_delete=models.CASCADE)

class ReservationClient(models.Model):
    id_reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    id_client = models.ForeignKey('Client', on_delete=models.CASCADE)

class ReservationClasse(models.Model):
    id_reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    classe = models.ForeignKey('Classe', on_delete=models.CASCADE)

class Passager(models.Model):
    id_passager = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255,null=True)
    prenom = models.CharField(max_length=255,null=True)
    dateN = models.DateField(null=True)
    categorie = models.ForeignKey('Categorie', on_delete=models.SET_NULL, null=True)

    #bdlt hna bch ndir id client yedih m la personne li rahi logged 
    client = models.ForeignKey(User, on_delete=models.CASCADE, default=None ,null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pass_field = models.CharField(max_length=255)

# zdtha l login 
    def __str__(self):
        return self.username

class Classe(models.Model):
    type = models.CharField(primary_key=True, max_length=255)
    capacite = models.IntegerField()
    prix = models.DecimalField(max_digits=15, decimal_places=2)

class Categorie(models.Model):
    id_categorie = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=15, decimal_places=2)

class AvionVol(models.Model):
    num_avion = models.ForeignKey('Avion', on_delete=models.CASCADE)
    num_vol = models.ForeignKey(Vol, on_delete=models.CASCADE)

class Avion(models.Model):
    num_avion = models.IntegerField(primary_key=True)
    autonomie = models.IntegerField()
    moteur = models.CharField(max_length=255)
   
    

    
   
    

class Avion_classe(models.Model):
  numavion= models.ForeignKey('Avion', on_delete=models.CASCADE)
  typeclasse= models.ForeignKey('Classe', on_delete=models.CASCADE)

 

