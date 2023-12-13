"""
Init Dev : TP10
Exercice 2 : Ecosystème
"""

def extinction_immediate(ecosysteme, animal):
    """
    renvoie True si animal s'éteint immédiatement dans l'écosystème faute
    de nourriture
    """
    for (predateur, proie) in ecosysteme.items():
        if predateur == animal:
            if proie in ecosysteme.keys():
                return False
    return True


def en_voie_disparition(ecosysteme, animal):
    """
    renvoie True si animal s'éteint est voué à disparaitre à long terme
    """
    i = 0
    while i < len(ecosysteme.keys()):
        if ecosysteme[animal] == None:
            return False
        elif extinction_immediate(ecosysteme,  animal):
            return True
        animal = ecosysteme[animal]
        i += 1
    return False

print(en_voie_disparition({ 'Loup': 'Mouton', 'Mouton':'Herbe', 'Dragon':'Lion', 'Lion':'Lapin', 'Herbe':None, 'Lapin':'Carotte', 'Requin':'Surfer'},'Lion'))

def animaux_en_danger(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en danger d'extinction immédiate"""
    ensemble = set()
    for (predateur, proie) in ecosysteme.items():
        if extinction_immediate(ecosysteme, predateur) and not proie == None:
            ensemble.add(predateur)
    return ensemble


def especes_en_voie_disparition(ecosysteme):
    """ renvoie l'ensemble des animaux qui sont en voués à disparaitre à long terme
    """
    ensemble = set()
    for predateur in ecosysteme.keys():
        if en_voie_disparition(ecosysteme, predateur):
            ensemble.add(predateur)
    return ensemble




