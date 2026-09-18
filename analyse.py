from cinetique import calculer_concentration

def simuler_evolution(c0, k, duree_heures):
    '''
    Simule l'évolution de la concentration au cours du temps.
    
    Paramètres :
    c0 : float, concentration initiale
    k : float, constante de vitesse
    duree_heures : int, durée de la simulation en heures

    Retour :
    list, liste des concentrations calculées 
    '''
    if c0 <= 0:
        raise ValueError("La concentration initiale doit être strictement positive.")
    if k <= 0:
        raise ValueError("La constante de vitesse doit être strictement positive.")
    if duree_heures <= 0:
        raise ValueError("La durée de la simulation doit être positive.")

    concentrations = []

    for heure in range(duree_heures + 1):
        concentration = calculer_concentration(c0, k, heure)
        concentrations.append(concentration)

    return concentrations

print(simuler_evolution(100, 0.15, 24))
