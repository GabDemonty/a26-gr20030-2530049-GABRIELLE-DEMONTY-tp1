from cinetique import calculer_concentration
from cinetique import calculer_demi_vie
from cinetique import convertir_concentration

concentration = calculer_concentration(100, 0.15, 1)
print (concentration)

demi_vie = calculer_demi_vie(0.15)
print (demi_vie)

conversion = convertir_concentration(25, "mg/L", "µg/mL")
print (conversion)
