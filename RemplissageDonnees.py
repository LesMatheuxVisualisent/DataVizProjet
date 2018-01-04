# -*- coding: utf-8 -*-

import os
import csv
import json
from math import floor

J = int(input("quelle dizaine ?"))

INP = "Donnees_Completes_" + str(J) + ".json"
f = open(INP,"r")
DonneeComplete = json.load(f)


I = 0
while I <= J :	
	i = 0
	while i < 10 :
		j = 0
		while j < 10 :
			DM = "DM_" + str(I) + "_par_" + str(J) + ".json"
			F= open(DM)
			data = json.load(F)
			
			for l, dep in enumerate(DonneeComplete['Dep']) :
				if l == 10*I + i :
					for m, dest in enumerate(dep['Destinations']) :
						if m == 10 * J + j :
							dest['Donnee'] = data['rows'][i]['elements'][j]
							
				if l == 10 * J + j :
					for m, dest in enumerate(dep['Destinations']) :
						if m == 10*I + i :
							dest['Donnee'] = data['rows'][i]['elements'][j]

			F.close()		
			j += 1	
		i += 1
	I += 1
		
f.close()

# écriture de la table crée dans un fichier json--------------------------------
J += 1

RES = "Donnees_Completes_" + str(J) + ".json"
resultat = open(RES,"w")
resultat.write(json.dumps(DonneeComplete))
resultat.close()

os.system("pause")


