from cinetique import calculer_concentration
from cinetique import calculer_demi_vie
from cinetique import convertir_concentration

concentration = calculer_concentration(100, 0.15, 1)
print (concentration)

demi_vie = calculer_demi_vie(0.15)
print (demi_vie)

conversion = convertir_concentration(25, "mg/L", "µg/mL")
print (conversion)


from cinetique import calculer_demi_vie
from analyse import simuler_evolution, analyser_resultats

#Paramètres de la situation
c0 = 100
k = 0.15
duree_heures = 24

seuil_min = 20
seuil_max = 80

#Simulation
liste_concentrations = simuler_evolution(c0, k, duree_heures)

#Analyse des résultats
rapport = analyser_resultats(
    liste_concentrations,
    seuil_min,
    seuil_max
)

#Calcul de la demi-vie
demi_vie = calculer_demi_vie(k)

#Affichage du rapport
print(rapport)
print(f"Demi vie calculée : {demi_vie} heures")