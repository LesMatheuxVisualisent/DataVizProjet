# -*- coding: utf-8 -*-

import os
import csv


#from csv import reader # permet de géner les fichiers csv
#from csv import writer # permet de géner les fichiers csv

import re # pour faire de l'analyse de texte
from glob import glob  # aussi pour la recherche dans du texte

#import Classe_Departement as CD


#la commande     glob(motif)       Liste les dossiers et les fichiers correspondants au motif




    

#affichage – itération sur chaque ligne


n = int(input("valeur dixaine de départ :")) #2
m = int(input("valeur dixaine à l'arrivée :")) #3
key = "AIzaSyBUOXA2bqxMQthVKRMlq3IjaRrixd3eZ0E"
mode = "driving"


def selection(N, T):
    L = []
    for i, row in enumerate(T) :
        if i >10 * N and i <= 10*(N+1): #pour i> 20 et i<= 30
            L.append(row[1])
    return "|".join(L)



#ouverture en lecture
f = open("Villes_de_France_par_taille.csv","r")

#lecture – utilisation du parseur csv
table = csv.reader(f,delimiter="	")

L1 = selection(n, table)

f.close()
    
#ouverture en lecture
f = open("Villes_de_France_par_taille.csv","r")

#lecture – utilisation du parseur csv
table = csv.reader(f,delimiter="	")

L2 = selection(m, table)

print()
print()
print()

print("https://maps.googleapis.com/maps/api/distancematrix/json?origins=",L1,"&destinations=",L2,"&mode=",mode,"&language=fr-FR&key=",key)




f.close()

os.system("pause")
