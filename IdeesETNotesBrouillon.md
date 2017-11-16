## Plaçons des idées et des notes ici.

### Requêtes pour générer la matrice de distance
16/11, Xian   
   
En effet, Googlemaps limite le nombre de requêtes à 2500 par jour (par compte). Du coup on ne peut que générer la matrice de distance pour 
environ 100 villes par jour.   
  
J'ai trouvé un autre service de carte du type open source qui peut être intéressant : ORSM.  
  
Cette service de carte permet   
    
- une recherche interactive efficace, comme sur Googlemaps
- de intéroger les distances de façon massive par des requêtes, seule condition étant que la matrice de distance ne dépasse pas 100*100 par requête.   
  
Lien (carte intéractive) : http://map.project-osrm.org/?z=7&center=44.699898%2C4.801025&loc=45.757814%2C4.832011&loc=43.296174%2C5.369953&hl=en&alt=0  
Lien (site officiel) : http://project-osrm.org/docs/v5.10.0/api/?language=Python#general-options on voit ici des API dans plusieurs langages.  
D'après un site français https://rgeomatic.hypotheses.org/710 ce truc-là existe aussi en R (qui serait le plus simple à utiliser pour nous),
or mon essai d'installation a échoué et sur le site officiel, l'API n'existe pas en R. Cependant, sur CRAN (site officiel des packages R)
ce package est "disponible" (https://cran.r-project.org/web/packages/osrm/README.html).   
   
On pourrait peut-être penser à (aprrendre à) utiliser cette carte.

