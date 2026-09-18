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


def analyser_resultats(liste_concentrations, seuil_min, seuil_max):
    '''
    Analyse les résultats de la simulation.

    Paramètres : 
    liste_concentrations : list, liste des concentrations calculées
    seuil_min : float, seuil minimum de la zone optimale
    seuil_max : float, seuil maximum de la zone optimale

    Retour : 
    str, rapport contenant la concentration maximale
    et le nombre d'heures en zone optimale
    '''
    if len(liste_concentrations) == 0:
        raise ValueError("La liste des concentrations ne peut pas être vide.")
    if seuil_min >= seuil_max:
        raise ValueError("seuil_min doit être < seuil_max")

    concentration_max = max(liste_concentrations)
    heures_optimales = 0
    for concentration in liste_concentrations:
        if concentration >= seuil_min and concentration <= seuil_max:
            heures_optimales += 1
    return f"Concentration maximale : {concentration_max}, Heures en zone optimale : {heures_optimales}"
liste = simuler_evolution(100, 0.15, 24)
