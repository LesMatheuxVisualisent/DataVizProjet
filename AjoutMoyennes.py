# -*- coding: utf-8 -*-

import os
import csv
import json
from math import floor


INP = "Donnees_Completes_10.json"
f = open(INP,"r")
DonneeComplete = json.load(f)

for dep in DonneeComplete['Dep'] :
	S = 0
	N = 0
	for dest in dep['Destinations'] :
		if int(dest['NoDep']) < 100 and dest['Donnee']['status'] != 'NOT_FOUND' and dest['Donnee']['status'] != 'ZERO_RESULTS' :
			S += dest['Donnee']['duration']['value'] 
			N += 1

	if N > 0 :
		dep['TpsAcces'] = S / (3600 * N)
	
	
f.close()



RES = "Donnees_Completes.json"
resultat = open(RES,"w")
resultat.write(json.dumps(DonneeComplete))
resultat.close()

#os.system("pause")


