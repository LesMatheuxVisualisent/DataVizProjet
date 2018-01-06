# -*- coding: utf-8 -*-

import os
import csv
import json
from math import floor
import xlrd
 
# ouverture du classeur
classeur = xlrd.open_workbook("Population_par_dep.xls")
 
# Récupération du nom de toutes les feuilles sous forme de liste
nom_des_feuilles = classeur.sheet_names()

print(nom_des_feuilles)

# Récupération de la première feuille
feuille = classeur.sheet_by_name('Départements')

#j = 8
#while j < 108 :
#        print(feuille.cell_value(j, 2), type(feuille.cell_value(j, 2)), int(feuille.cell_value(j, 8)))
#        j += 1

def MiseAJour() :

        INP = "Donnees_CompletesHM.json"
        f = open(INP,"r")
        DonneeComplete = json.load(f)

        for dep in DonneeComplete['Dep'] :
                dep.update({'Population' : 'NC'})
                if dep['NoDep'] != '2A' and dep['NoDep'] != '2B' and int(dep['NoDep']) < 100 :
                        print(dep['NoDep'])
                        pop = 0
                        i = 8
                        while i < 108 :
                                if feuille.cell_value(i, 2) != '2A' and feuille.cell_value(i, 2) != '2B' and str(int(feuille.cell_value(i, 2))) == str(dep['NoDep']) :
                                        print(int(feuille.cell_value(i, 2)), str(dep['NoDep']), feuille.cell_value(i, 8))
                                        pop += int(feuille.cell_value(i, 8))
                                i += 1
                        dep.update({'Population' : pop})


        f.close()



        RES = "Donnees_CompletesHMP.json"
        resultat = open(RES,"w")
        resultat.write(json.dumps(DonneeComplete))
        resultat.close()



#MiseAJour()

def ajoutPopDestinations() :

	INP = "Donnees_CompletesHMP.json"
	f = open(INP,"r")
	Donnee = json.load(f)

	for destination in Donnee['Dep']:
		if destination['Population'] != 'NC' :
			for dep in Donnee['Dep']:
				if dep['Population'] != 'NC' :
					for dest in dep['Destinations'] :
						if dest['NoDep'] == destination['NoDep'] :
							dest.update({'Population' : destination['Population'] })




	RES = "Donnees_CompletesHMPP.json"
	resultat = open(RES,"w")
	resultat.write(json.dumps(Donnee))
	resultat.close()



#ajoutPopDestinations()
        
def calculCoefficient() :
        m = 1000
        depmin = 'NC'
        M = 0
        depmax = 'NC'
        pop = 0
        INP = "Donnees_CompletesHMPP.json"
        f = open(INP,"r")
        Donnee = json.load(f)

        for dep in Donnee['Dep'] :
                if dep['NoDep'] != '2A' and dep['NoDep'] != '2B' and int(dep['NoDep']) < 100 :
                        pop += dep['Population']

        print(pop)

        
        for dep in Donnee['Dep'] :
                coef = 'NC'
                if dep['NoDep'] != '2A' and dep['NoDep'] != '2B' and int(dep['NoDep']) < 100 :
                        S = 0
                        for dest in dep['Destinations'] :
                                if dest['NoDep'] != '2A' and dest['NoDep'] != '2B' and int(dest['NoDep']) < 100 : #dest['Donnee']['status'] != 'NOT_FOUND' and dest['Donnee']['status'] != 'ZERO_RESULTS' :
                                        S += dest['Donnee']['duration']['value'] * float(dest['Population']) / 3600
                                        

                        coef = S / pop
                        if coef < m :
                                m = coef
                                depmin = dep['NoDep']
                        if coef > M :
                                M = coef
                                depmax = dep['NoDep']
                        
        print(m, M, 'depmin : ' , depmin, 'depmax : ', depmax)

                
        f.close()
        



        #RES = "Donnees_CompletesHMPPC.json"
        #resultat = open(RES,"w")
        #resultat.write(json.dumps(Donnee))
        #resultat.close()        


calculCoefficient()

def formatageHeureMinutes() :

        
        INP = "Donnees_CompletesHMPPC.json"
        f = open(INP,"r")
        DonneeComplete = json.load(f)

        for dep in DonneeComplete['Dep'] :
                tps = 'NC'
                if dep['NoDep'] != '2A' and dep['NoDep'] != '2B' and int(dep['NoDep']) < 100 :
                        heure = str(floor(dep['Coefficient']))
                        minutes = str(floor( (dep['Coefficient']-floor(dep['Coefficient']))*60 ))
                        if minutes == '0' :		
                                tps = heure + ' h '
                        elif minutes == '1' :
                                tps = heure + ' h ' + minutes + ' minute'
                        else :
                                tps = heure + ' h ' + minutes + ' minutes'
                        
                dep.update({'CoefficientFormate' : tps })
                
                
                
        f.close()



        RES = "Donnees_CompletesHMPPCHM.json"
        resultat = open(RES,"w")
        resultat.write(json.dumps(DonneeComplete))
        resultat.close()


#formatageHeureMinutes()


def maxtempsacces() :

        m = 1000
        depmin = 'NC'
        M = 0
        depmax = 'NC'
        INP = "Donnees_CompletesHMPPCHM.json"
        f = open(INP,"r")
        Donnee = json.load(f)

        for dep in Donnee['Dep'] :
                if dep['TpsAcces'] != 'NC' :
                        if dep['TpsAcces'] < m :
                                m = dep['TpsAcces']
                                depmin = dep['NoDep']
                        if dep['TpsAcces'] > M :
                                M = dep['TpsAcces']
                                depmax = dep['NoDep']
                        
        print(m, M, 'depmin : ' , depmin, 'depmax : ', depmax)
        f.close()

maxtempsacces()
        
#os.system("pause")


