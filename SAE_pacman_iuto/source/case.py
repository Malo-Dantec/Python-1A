"""
            SAE1.02 PACMAN IUT'O
         BUT1 Informatique 2023-2024

        Module case.py
        Ce module contient l'implémentation des cases du plateau de jeu
"""
import const

def Case(mur=False, objet=const.AUCUN, pacmans_presents=None, fantomes_presents=None):
    """Permet de créer une case du plateau

    Args:
        mur (bool, optional): un booléen indiquant si la case est un mur ou un couloir.
                Defaults to False.
        objet (str, optional): un caractère indiquant l'objet qui se trouve sur la case.
                const.AUCUN indique qu'il n'y a pas d'objet sur la case. Defaults to const.AUCUN.
        pacmans_presents (set, optional): un ensemble indiquant la liste des pacmans
                se trouvant sur la case. Defaults to None.
        fantomes_presents (set, optional): un ensemble indiquant la liste des fantomes
                se trouvant sur la case. Defaults to None.

    Returns:
        dict: un dictionnaire représentant une case du plateau
    """
    dico = dict()
    dico['mur'] = mur
    dico['objet'] = objet
    dico['pacmans_present'] = pacmans_presents
    dico['fantome_present'] = fantomes_presents
    return dico
    

def est_mur(case):
    """indique si la case est un mur ou non

    Args:
        case (dict): la case considérée

    Returns:
        bool: True si la case est un mur et False sinon
    """
    return case['mur'] 




def get_objet(case):
    """retourne l'identifiant de l'objet qui se trouve sur la case. const.AUCUN indique l'absence d'objet.

    Args:
        case (dict): la case considérée

    Returns:
        str: l'identifiant de l'objet qui se trouve sur la case.
    """
    return case['objet']


def get_pacmans(case):
    """retourne l'ensemble des pacmans qui sont sur la case

    Args:
        case (dict): la case considérée

    Returns:
        set: l'ensemble des identifiants de pacmans présents su la case.
    """
    if case['pacmans_present'] == None:
        return set()
    else:
        return case['pacmans_present']

def get_fantomes(case):
    """retourne l'ensemble des fantomes qui sont sur la case

    Args:
        case (dict): la case considérée

    Returns:
        set: l'ensemble des identifiants de fantomes présents su la case.
    """
    if case['fantome_present'] == None:
        return set()
    else:
        return case['fantome_present']
    



def get_nb_pacmans(case):
    """retourne le nombre de pacmans présents sur la case

    Args:
        case (dict): la case considérée

    Returns:
        int: le nombre de pacmans présents sur la case.
    """
    if case['pacmans_present'] == None:
        return 0
    else: 
        return len(case['pacmans_present'])

def get_nb_fantomes(case):
    """retourne le nombre de fantomes présents sur la case

    Args:
        case (dict): la case considérée

    Returns:
        int: le nombre de fantomes présents sur la case.
    """
    if case['fantome_present'] == None:
        return 0
    else: 
        return len(case['fantome_present'])

def poser_objet(case, objet):
    """Pose un objet sur la case. Si un objet était déjà présent ce dernier disparait.
        Si la case est un mur, l'objet n'est pas mis dans la case.

    Args:
        case (dict): la case considérée
        objet (str): identifiant d'objet. const.AUCUN indiquant que plus aucun objet se
                trouve sur la case.
    """
    if est_mur(case) :
        return None
    else :
        case['objet'] = objet

def prendre_objet(case):
    """Enlève l'objet qui se trouve sur la case et retourne l'identifiant de cet objet.
        Si aucun objet se trouve sur la case la fonction retourne const.AUCUN.

    Args:
        case (dict): la case considérée

    Returns:
        char: l'identifiant de l'objet qui se trouve sur la case.
    """
    if get_objet(case) == const.AUCUN :
        return const.AUCUN
    else:
        temp = case['objet'] 
        case['objet'] = const.AUCUN
        return temp


def poser_pacman(case, pacman):
    """Pose un nouveau pacman sur la case.
    Si le pacman était déjà sur la case la fonction ne fait rien
    Si la case est un mur, le pacman est quand-même posé (pouvoir de passe-muraille)

    Args:
        case (dict): la case considérée
        pacman (str): identifiant du pacman à ajouter sur la case
    """
    if case['pacmans_present'] == None:
        case['pacmans_present'] = {pacman}
    else:
        case['pacmans_present'].add(pacman)





def prendre_pacman(case, pacman):
    """Enlève le pacman dont l'identifiant est passé en paramètre de la case.
        La fonction retourne True si le joueur était bien sur la case et False sinon.

    Args:
        case (dict): la case considérée
        pacman (str): l'identifiant du pacman à enlever

    Returns:
        bool: True si le joueur était bien sur la case et False sinon.
    """
    if case['pacmans_present'] != None and pacman in case['pacmans_present'] :
        case['pacmans_present'].remove(pacman)
        return True
    else:
        return False



def poser_fantome(case, fantome):
    """Pose un nouveau fantome sur la case
        si le fantome était déjà sur la case, la fonction ne fait rien
        si la case est un mur la fonction ne fait rien

    Args:
        case (dict): la case considérée
        fantome (str): identifiant du fantome à ajouter sur la case
    """

    if case['fantome_present'] is None and not est_mur(case):
        case['fantome_present'] = {fantome}
    elif case['fantome_present'] is not None and not est_mur(case) and fantome not in case['fantome_present']:
        case['fantome_present'].add(fantome)


def prendre_fantome(case, fantome):
    """Enlève le fantome dont l'identifiant est passé en paramètre de la case.
        La fonction retourne True si le fantome était bien sur la case et False sinon.

    Args:
        case (dict): la case considérée
        fantome (str): l'identifiant du fantome à enlever

    Returns:
        bool: True si le fantome était bien sur la case et False sinon.
    """
    if case['fantome_present'] != None and fantome in case['fantome_present'] :
        case['fantome_present'].remove(fantome)
        return True
    else:
        return False
