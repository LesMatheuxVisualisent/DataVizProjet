# -*- coding: utf-8 -*-

import os
import csv
import json
from math import floor

i = int(input("Numero de ville de départ (entre 1 et 30) :"))
j = int(input("Numero de ville d'arrivée (entre 1 et 30) :"))

i-= 1
j-= 1


i_unit = int(i % 10)
j_unit= int(j % 10)

i_dix = int((i - i_unit)/10)
j_dix = int((j-j_unit )/10)

DM = "Distance_matrix_" + str(i_dix) + "_par_" + str(j_dix) + ".json"

f= open(DM)


data = json.load(f)




#sélectionner le temps de trajet et la distance entre la ville i et j:
def dist_temps (I, J):
    dist = data['rows'][I]['elements'][J]['distance']['text']
    temps = data['rows'][I]['elements'][J]['duration']['text']
    return (dist, temps)

Ville1 = data['origin_addresses'][i_unit].split(",")[0]
Ville2 = data['destination_addresses'][j_unit].split(",")[0]


print()
print()

print("de", Ville1, "à", Ville2, ":", dist_temps(i_unit,j_unit))




def temps_moy (I) :
    UUnit = int(I % 10)
    DDix = int((I - UUnit)/10)
    S = 0
    k = 0
    while k < 30 :
        Unit= int(k % 10)
        Dix = int((k-Unit )/10)
        Daime = "Distance_matrix_" + str(DDix) +"_par_" + str(Dix) + ".json"
        F= open(Daime)
        Data = json.load(F)
        S += int(Data['rows'][UUnit]['elements'][Unit]['duration']['value'])
        F.close()
        k += 1
    return S / 30

print()
print()
l = 0
while l < 30 :
    print("le temps moyen pour accéder à la ville", l+ 1, "est", temps_moy(l))
    l += 1


f.close()



os.system("pause")


