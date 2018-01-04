# -*- coding: utf-8 -*-

import os
import csv
import json
from math import floor






# Instanciation de la table de données complete----------------------------------------------

DonneeComplete =  {'Dep' : []}

# on charge l'ensemble des départements et leur capitale, avec pour chacun la structure:
# { 'NoDep' : no de departement , 'nomCap' : nom de la ville capitale , "ClsmntVille" : numero dans classement par taille, 'TpsAcces' : moyenne nationale du temps d'acces, 'Destinations' : liste des départements destination } 

CSV = open("DepetCap.csv","r", newline='')
tableDep = csv.reader(CSV)



for line in CSV:
	dep = { 'NoDep' : int(line.split(',')[0]), 'nomCap' : line.split(',')[2], 'TpsAcces' : 'NC', 'Destinations' : [] }
	DonneeComplete['Dep'].append(dep)
	
CSV.close()


for dep in DonneeComplete['Dep']:
	for deps in DonneeComplete['Dep'] :
		dest = { 'NoDep' : deps['NoDep'], 'nomCap' : deps['nomCap'], 'Donnee' : 'NC' }
		dep['Destinations'].append(dest)


# puis on charge les distances par ordre donné par le classement des villes:-------------------------






J = 0
while J <= 2 :
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
	J += 1
	

# écriture de la table crée dans un fichier json--------------------------------

resultat = open("Donnees_Completes_3.json","w")
resultat.write(json.dumps(DonneeComplete))
resultat.close()

os.system("pause")


