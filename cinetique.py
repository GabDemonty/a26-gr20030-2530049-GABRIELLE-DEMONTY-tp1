import math
    
def calculer_concentration(c0, k, temps):
    '''
    Calcule la concentration restante selon le temps
    Paramètres : 
    c0 : float, concetration initiale
    k : float, constante de vitesse
    temps : float, temps écoulé

    Retour : 
    float, concentration restante
    '''
    if c0 < 0:    
        raise ValueError("La concentration initaile doit être positive ou nulle.")
    if k <= 0:
        raise ValueError("La constante de vitesse doit être strictement positive.")
    if temps < 0:
        raise ValueError("Le temps doit être positif ou nul.")

    concentration = c0 * math.exp(-k * temps)

    return concentration

def calculer_demi_vie(k):
    '''
    Calcule le temps de demi-vie à partir de la constante k.
    
    Paramètres : 
    k : float, constante de vitesse
    
    Retour : 
    float, temps de demi-vie
    '''
    if k <= 0:
        raise ValueError("La constante de vitesse doit être strictement positive.")

    demi_vie = math.log(2) / k

    return demi_vie


def convertir_concentration (valeur, unite_source, unite_cible):
    '''
    Convertit une concentration entre mg/L et µg/mL.
    
    Paramètres : 
    valeur : float, valeur de la concentration
    unite_source : str, unité de départ
    unite_cible : str, unité d'arrivée

    Retour :
    float, valeur de la concentration convertie
    '''
    if valeur < 0:
        raise ValueError("La valeur de la concentration doit être positive ou nulle.")
    if unite_source == "mg/L" and unite_cible == "µg/mL":
        return valeur * 1000
    elif unite_source == "µg/mL" and unite_cible == "mg/L":
        return valeur / 1000
    else:
        raise ValueError("Conversion non supportée.")

    def evaluer_niveau(concentration, seuil_min, seuil_max_):
        '''
        Détermine le niveau d'une concentration selon deu seuils.
        
        Paramètres : 
        concentration : float, concentration à évaluer
        seuil_min : float, seuil minimum de la zone optimale
        seuil_max : float, seuil maximum de la zone optimale

        Retour : 
        str, niveau de la concentration
        '''
        if seuil_min >= seuil_max_:
            raise ValueError("seuil_min doit être < au seuil_max.")
        if concentration < seuil_min:
            return 'INSUFFISANT'
        elif concentration <= seuil_max:
            return 'OPTIMAL'
        else:
            return 'TOXIQUE / CRITIQUE'
