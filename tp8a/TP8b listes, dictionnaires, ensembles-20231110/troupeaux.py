# TP8 B - Manipuler des listes, ensembles et dictionnaires


def total_animaux(troupeau):
    """ Calcule le nombre total d'animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        int: le nombre total d'animaux dans le troupeau
    """
    cpt = 0
    for animaux in troupeau.values():
        cpt += animaux
    return cpt


def tous_les_animaux(troupeau):
    """ Détermine l'ensemble des animaux dans un troupeau

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        set: l'ensemble des animaux du troupeau
    """
    ensemble_animaux = set()
    for animaux in troupeau.keys():
        ensemble_animaux.add(animaux)
    return ensemble_animaux


def specialise(troupeau):
    """ Vérifie si le troupeau contient 30 individus ou plus d'un même type d'animal 

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient 30 (ou plus) individus d'un même type d'animal,
        False sinon 
    """
    for animaux in troupeau.values():
        if animaux >= 30:
            return True
    return False


def le_plus_represente(troupeau):
    """ Recherche le nom de l'animal qui a le plus d'individus dans le troupeau
    
    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        str: le nom de l'animal qui a le plus d'individus  dans le troupeau
        None si le troupeau est vide) 
    
    """
    animal = None
    plus_grand_nombre = 0
    for (animaux,nombre) in troupeau.items():
        if nombre > plus_grand_nombre:
            plus_grand_nombre = nombre
            animal = animaux
    return animal




def quantite_suffisante(troupeau):
    """ Vérifie si le troupeau contient au moins 5 individus de chaque type d'animal

    Args:
        troupeau (dict): un dictionnaire modélisant un troupeau {nom_animaux: nombre}

    Returns:
        bool: True si le troupeau contient au moins 5 individus de chaque type d'animal
        False sinon    
    """
    for animaux in troupeau.values():
        if animaux < 5:
            return False
    return True


def reunion_troupeaux(troupeau1, troupeau2):
    """ Simule la réunion de deux troupeaux

    Args:
        troupeau1 (dict): un dictionnaire modélisant un premier troupeau {nom_animaux: nombre}
        troupeau2 (dict): un dictionnaire modélisant un deuxième troupeau        

    Returns:
        dict: le dictionnaire modélisant la réunion des deux troupeaux    
    """
    reunion = dict()
    if troupeau1 == dict():
        return troupeau2
    elif troupeau2 == dict():
        return troupeau1
    else:
        for (animaux,nombre) in troupeau1.items():
            reunion[animaux]=nombre
        for (animaux,nombre) in troupeau2.items():
            if animaux in reunion.keys():
                reunion[animaux]+=nombre
            else:
                reunion[animaux]=nombre
    return reunion




