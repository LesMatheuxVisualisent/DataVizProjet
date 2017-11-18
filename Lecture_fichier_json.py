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



f.close()



os.system("pause")


