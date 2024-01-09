"""
Permet de modéliser un le_plateau de jeu avec :
    - une matrice qui contient des nombres entiers
    - chaque nombre entier correspond à un item :
      MUR, COULOIR, PERSONNAGE, FANTOME
"""
import matrice

MUR = 1
COULOIR = 0
PERSONNAGE = 2
FANTOME = 3

NORD = 'z'
OUEST = 'q'
SUD = 'w'
EST = 's'

dico_matrice = (9, 9, {(0, 0): 2, (0, 1): 1, (0, 2): 1, (0, 3): 1, (0, 4): 1, (0, 5): 1, (0, 6): 1, (0, 7): 1, (0, 8): 1, (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 1, (1, 4): 1, (1, 5): 1, (1, 6): 1, (1, 7): 1, (1, 8): 1, (2, 0): 1, (2, 1): 1, (2, 2): 0, (2, 3): 1, (2, 4): 0, (2, 5): 0, (2, 6): 0, (2, 7): 0, (2, 8): 1, (3, 0): 1, (3, 1): 1, (3, 2): 0, (3, 3): 1, (3, 4): 0, (3, 5): 1, (3, 6): 1, (3, 7): 0, (3, 8): 1, (4, 0): 1, (4, 1): 1, (4, 2): 0, (4, 3): 0, (4, 4): 0, (4, 5): 0, (4, 6): 0, (4, 7): 0, (4, 8): 1, (5, 0): 1, (5, 1): 1, (5, 2): 1, (5, 3): 0, (5, 4): 1, (5, 5): 1, (5, 6): 1, (5, 7): 0, (5, 8): 1, (6, 0): 1, (6, 1): 1, (6, 2): 1, (6, 3): 0, (6, 4): 1, (6, 5): 1, (6, 6): 1, (6, 7): 0, (6, 8): 1, (7, 0): 1, (7, 1): 1, (7, 2): 1, (7, 3): 0, (7, 4): 0, (7, 5): 0, (7, 6): 0, (7, 7): 0, (7, 8): 1, (8, 0): 1, (8, 1): 1, (8, 2): 1, (8, 3): 1, (8, 4): 1, (8, 5): 1, (8, 6): 1, (8, 7): 0, (8, 8): 3})


def init(nom_fichier="./labyrinthe1.txt"):
    """Construit le plateau de jeu de la façon suivante :
        - crée une matrice à partir d'un fichier texte qui contient des COULOIR et MUR
        - met le PERSONNAGE en haut à gauche cad à la position (0, 0)
        - place un FANTOME en bas à droite
    Args:
        nom_fichier (str, optional): chemin vers un fichier csv qui contient COULOIR et MUR.
        Defaults to "./labyrinthe1.txt".

    Returns:
        le plateau de jeu avec les MUR, COULOIR, PERSONNAGE et FANTOME
    """
    ma_matrice = matrice.charge_matrice(nom_fichier, type_valeur='int')
    matrice.set_val(ma_matrice, 0, 0, PERSONNAGE)
    matrice.set_val(ma_matrice, matrice.get_nb_lignes(ma_matrice)-1, matrice.get_nb_colonnes(ma_matrice)-1, FANTOME)
    return ma_matrice
# print(matrice.affiche(init()))
# print(matrice.affiche2(init()))


def les_positions_du_plateau(le_plateau):
    return le_plateau[2]
# print(les_positions_du_plateau(dico_matrice))
def est_sur_le_plateau(le_plateau, position):
    """Indique si la position est bien sur le plateau

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        [boolean]: True si la position est bien sur le plateau
    """
    if position in les_positions_du_plateau(le_plateau):
        return True
    return False


def get(le_plateau, position):
    """renvoie la valeur de la case qui se trouve à la position donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple d'entiers de la forme (no_ligne, no_colonne)

    Returns:
        int: la valeur de la case qui se trouve à la position donnée ou
             None si la position n'est pas sur le plateau
    """
    if est_sur_le_plateau(le_plateau, position):
        return matrice.get_val(le_plateau, position[0], position[1])
    return None


def est_un_mur(le_plateau, position):
    """détermine s'il y a un mur à la poistion donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple d'entiers de la forme (no_ligne, no_colonne)

    Returns:
        bool: True si la case à la position donnée est un MUR, False sinon
    """
    if get(le_plateau, position) == MUR:
        return True
    return False


def contient_fantome(le_plateau, position):
    """Détermine s'il y a un fantôme à la position donnée

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        bool: True si la case à la position donnée est un FANTOME, False sinon
    """
    if get(le_plateau, position) == FANTOME:
        return True
    return False


def est_la_sortie(le_plateau, position):
    """Détermine si la position donnée est la sortie
       cad la case en bas à droite du labyrinthe

    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        bool: True si la case à la position donnée est la sortie, False sinon
    """

    pos_sortie = (le_plateau[0]-1, le_plateau[1]-1)
    if position == pos_sortie:
        return True
    return False


def position_valide(le_plateau, position):
    return est_sur_le_plateau(le_plateau, position) and not est_un_mur(le_plateau, position)
          

def position_direction(le_plateau, position, direction):
    if direction == SUD and position_valide(le_plateau, (position[0] + 1, position[1])):
        return (position[0] + 1, position[1])
    elif direction == EST and position_valide(le_plateau, (position[0], position[1] + 1)):
        return (position[0], position[1] + 1)
    elif direction == NORD and position_valide(le_plateau, (position[0] - 1, position[1])):
        return (position[0] - 1, position[1])
    elif direction == OUEST and position_valide(le_plateau, (position[0], position[1] - 1)):
        return (position[0], position[1] - 1)


def direction_valide(le_plateau, position, direction):
    return position_valide(le_plateau, position_direction(le_plateau, position, direction))
          

def deplace_personnage(le_plateau, personnage, direction):
    """déplace le PERSONNAGE sur le plateau si le déplacement est valide
       Le personnage ne peut pas sortir du plateau ni traverser les murs
       Si le déplacement n'est pas valide, le personnage reste sur place

    Args:
        le_plateau (plateau): un plateau de jeu
        personnage (tuple): la position du personnage sur le plateau
        direction (str): la direction de déplacement SUD, EST, NORD, OUEST

    Returns:
        [tuple]: la nouvelle position du personnage
    """
    nouvelle_pos = personnage
    if direction_valide(le_plateau, personnage, direction):
        nouvelle_pos = position_direction(le_plateau, personnage, direction)
    matrice.set_val(le_plateau, personnage[0], personnage[1], COULOIR)
    matrice.set_val(le_plateau, nouvelle_pos[0], nouvelle_pos[1], PERSONNAGE)
    return nouvelle_pos


def voisins(le_plateau, position):
    """Renvoie l'ensemble des positions cases voisines accessibles de la position renseignées
       Une case accessible est une case qui est sur le plateau et qui n'est pas un mur
    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        set: l'ensemble des positions des cases voisines accessibles
    """
    return set(pos for pos in [(position[0] + 1, position[1]), (position[0] - 1, position[1]), (position[0], position[1]+1), (position[0], position[1]-1)] if position_valide(le_plateau, pos))

def voisins_chemin(le_plateau, position):
    """Renvoie l'ensemble des positions cases voisines accessibles de la position renseignées
       Une case accessible est une case qui est sur le plateau et qui n'est pas un mur
    Args:
        le_plateau (plateau): un plateau de jeu
        position (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        set: l'ensemble des positions des cases voisines accessibles
    """
    return set(pos for pos in [(position[0] + 1, position[1]), (position[0] - 1, position[1]), (position[0], position[1]+1), (position[0], position[1]-1)] if est_sur_le_plateau(le_plateau, pos))

def pos_par_valeur(le_plateau, valeur):
    return set(pos for pos in les_positions_du_plateau(le_plateau) if get(le_plateau, pos) == valeur)


def fabrique_le_calque(le_plateau, position_depart):
    """fabrique le calque d'un labyrinthe en utilisation le principe de l'inondation :
       
    Args:
        le_plateau (plateau): un plateau de jeu
        position_depart (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        matrice: une matrice qui a la taille du plateau dont la case qui se trouve à la
       position_de_depart est à 0 les autres cases contiennent la longueur du
       plus court chemin pour y arriver (les murs et les cases innaccessibles sont à None)
    """
    calque = matrice.new_matrice(matrice.get_nb_lignes(le_plateau), matrice.get_nb_colonnes(le_plateau), None)
    matrice.set_val(calque, position_depart[0], position_depart[1], 0)
    nombre = 0
    changement = True
    while changement:
        changement = False
        for pos in pos_par_valeur(calque, nombre):
            for voisin in voisins(calque, pos):
                if position_valide(le_plateau, voisin) and get(calque, voisin) is None:
                    matrice.set_val(calque, voisin[0], voisin[1], get(calque, pos) + 1)
                    changement = True
        nombre += 1
    return calque

# print()
# print(fabrique_le_calque(dico_matrice, (4, 2)))
# print(matrice.affiche(fabrique_le_calque(dico_matrice, (4, 5))))


def fabrique_chemin(le_plateau, position_depart, position_arrivee):
    """Renvoie le plus court chemin entre position_depart position_arrivee

    Args:
        le_plateau (plateau): un plateau de jeu
        position_depart (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 
        position_arrivee (tuple): un tuple de deux entiers de la forme (no_ligne, no_colonne) 

    Returns:
        list: Une liste de positions entre position_arrivee et position_depart
        qui représente un plus court chemin entre les deux positions
    """
    pos = position_arrivee
    calque = fabrique_le_calque(le_plateau, position_depart)
    chemin = []
    while pos != position_depart:
        chemin.append(pos)
        for voisin in voisins_chemin(calque, pos):
            if get(calque, voisin) == get(calque, pos) - 1:
                pos = voisin
    return chemin

# print(fabrique_chemin(dico_matrice, (4, 5), (8, 8)))
# print(fabrique_chemin(dico_matrice, (5, 3), (8, 8)))

def deplace_fantome(le_plateau, fantome, personnage):
    """déplace le FANTOME sur le plateau vers le personnage en prenant le chemin le plus court

    Args:
        le_plateau (plateau): un plateau de jeu
        fantome (tuple): la position du fantome sur le plateau
        personnage (tuple): la position du personnage sur le plateau

    Returns:
        [tuple]: la nouvelle position du FANTOME
    """
    chemin = fabrique_chemin(le_plateau, personnage, fantome)
    if len(chemin) >= 2:
        matrice.set_val(le_plateau, chemin[1][0], chemin[1][1], FANTOME)
        matrice.set_val(le_plateau, fantome[0], fantome[1], COULOIR)
        return chemin[1]
    return fantome
# print(deplace_fantome(dico_matrice, (8,8), (7,4)))
# print(deplace_fantome(dico_matrice, (8,8), (8,8)))
# print(deplace_fantome(dico_matrice, (8,8), (5,8)))
# print(deplace_fantome(dico_matrice, (8,8), (2,1)))
# print(deplace_fantome(dico_matrice, (8,8), (6,6)))

