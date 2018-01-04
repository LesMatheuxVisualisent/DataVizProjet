
# -*- coding: utf-8 -*-

import os
import csv


#from csv import reader # permet de géner les fichiers csv
#from csv import writer # permet de géner les fichiers csv

import re # pour faire de l'analyse de texte
from glob import glob  # aussi pour la recherche dans du texte

C = True

while C == True :

    n = int(input("valeur dixaine de départ :")) #2
    m = int(input("valeur dixaine à l'arrivée :")) #3
    cle = input("quelle clé ?")
    mode = "driving"

    if cle == '1' :
	    key = "AIzaSyBUOXA2bqxMQthVKRMlq3IjaRrixd3eZ0E"
    else :
	    key = 'AIzaSyDubqOhlWnFiE4OWSD4R6nKmh6oSf7zY0k'

    def selection(N, T):
        L = []
        for i, row in enumerate(T) :
            if i >= 10 * N and i < 10*(N+1): #pour i>= 20 et i< 30
                L.append(row[2])
        return "|".join(L)



    #ouverture en lecture
    f = open("DepetCap.csv","r")

    #lecture – utilisation du parseur csv
    table = csv.reader(f,delimiter=",")

    L = selection(n, table)

    f.close()

    f = open("DepetCap.csv","r")

    #lecture – utilisation du parseur csv
    table = csv.reader(f,delimiter=",")
    K = selection(m, table)

    print()
    print()

    print("https://maps.googleapis.com/maps/api/distancematrix/json?origins=",L,"&destinations=",K,"&mode=",mode,"&language=fr-FR&key=",key)

    print()
    print()
    print()
    
    f.close()


    R = input("Génération supplémentaire ?")
    if R == 'n' or R == 'N' :
        C = False





os.system("pause")
