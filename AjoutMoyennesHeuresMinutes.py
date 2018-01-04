# -*- coding: utf-8 -*-

import os
import csv
import json
from math import floor


INP = "Donnees_Completes.json"
f = open(INP,"r")
DonneeComplete = json.load(f)

for dep in DonneeComplete['Dep'] :
	tps = 'NC'
	if dep['TpsAcces'] != 'NC' :
		heure = str(floor(dep['TpsAcces']))
		minutes = str(floor( (dep['TpsAcces']-floor(dep['TpsAcces']))*60 ))
		if minutes == '0' :		
			tps = heure + ' h '
		elif minutes == '1' :
			tps = heure + ' h ' + minutes + ' minute'
		else :
			tps = heure + ' h ' + minutes + ' minutes'
		
	dep.update({'TpsFormate' : tps })
	
	
	
f.close()



RES = "Donnees_CompletesHM.json"
resultat = open(RES,"w")
resultat.write(json.dumps(DonneeComplete))
resultat.close()

#os.system("pause")


