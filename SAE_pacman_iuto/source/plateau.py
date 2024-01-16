"""
            SAE1.02 PACMAN IUT'O
         BUT1 Informatique 2023-2024

        Module plateau.py
        Ce module contient l'implémentation de la structure de données
        qui gère le plateau jeu aussi qu'un certain nombre de fonctions
        permettant d'observer le plateau et d'aider l'IA à prendre des décisions
"""
import const
import case
import random

def get_nb_lignes(plateau):
    """retourne le nombre de lignes du plateau

    Args:
        plateau (dict): le plateau considéré

    Returns:
        int: le nombre de lignes du plateau
    """
    return plateau['lig']

def get_nb_colonnes(plateau):
    """retourne le nombre de colonnes du plateau

    Args:
        plateau (dict): le plateau considéré

    Returns:
        int: le nombre de colonnes du plateauposition_depart
    """
    return plateau['col']
    
def pos_ouest(plateau, pos):
    """retourne la position de la case à l'ouest de pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position
    Returns:
        int: un tuple d'entiers
    """
    max_col = get_nb_colonnes(plateau)
    (pos_lig, pos_col) = pos
    voisin_ouest = (pos_lig, pos_col-1)
    if voisin_ouest[1] < 0:
        voisin_ouest = (pos_lig, max_col-1)
    return voisin_ouest


def pos_est(plateau, pos):
    """retourne la position de la case à l'est de pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position
    Returns:
        int: un tuple d'entiers
    """
    max_col = get_nb_colonnes(plateau)
    (pos_lig, pos_col) = pos
    voisin_est = (pos_lig, pos_col+1)
    if voisin_est[1] >= max_col:
        voisin_est = (pos_lig, 0)
    return voisin_est


def pos_nord(plateau, pos):
    """retourne la position de la case au nord de pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position
    Returns:
        int: un tuple d'entiers
    """
    max_lig = get_nb_lignes(plateau)
    (pos_lig, pos_col) = pos
    voisin_nord = (pos_lig-1, pos_col)
    if voisin_nord[0] < 0:
        voisin_nord = (max_lig-1, pos_col)
    return voisin_nord


def pos_sud(plateau, pos):
    """retourne la position de la case au sud de pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position
    Returns:
        int: un tuple d'entiers
    """
    max_lig = get_nb_lignes(plateau)
    (pos_lig, pos_col) = pos
    voisin_sud = (pos_lig+1, pos_col)
    if voisin_sud[0] >= max_lig:
        voisin_sud = (0, pos_col)
    return voisin_sud


def pos_arrivee(plateau,pos,direction):
    """ calcule la position d'arrivée si on part de pos et qu'on va dans
    la direction indiquée en tenant compte que le plateau est un tore
    si la direction n'existe pas la fonction retourne None
    Args:
        plateau (dict): Le plateau considéré
        pos (tuple): une paire d'entiers qui donne la position de départ
        direction (str): un des caractère NSEO donnant la direction du déplacement

    Returns:
        None|tuple: None ou une paire d'entiers indiquant la position d'arrivée
    """
    if direction == 'N':
        return pos_nord(plateau, pos)
    if direction == 'S':
        return pos_sud(plateau,pos)
    if direction == 'O':
        return pos_ouest(plateau,pos)
    if direction == 'E':    
        return pos_est(plateau,pos)
    return None


def get_case(plateau, pos):
    """retourne la case qui se trouve à la position pos du plateau

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        dict: La case qui se situe à la position pos du plateau
    """
    (pos_lig, pos_col) = pos
    return plateau['carte'][pos_lig][pos_col]

def get_objet(plateau, pos):
    """retourne l'objet qui se trouve à la position pos du plateau

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        str: le caractère symbolisant l'objet
    """
    la_case = get_case(plateau, pos)
    return case.get_objet(la_case)

def poser_pacman(plateau, pacman, pos):
    """pose un pacman en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        pacman (str): la lettre représentant le pacman
        pos (tuple): une paire (lig,col) de deux int
    """
    case.poser_pacman(get_case(plateau, pos), pacman)

def poser_fantome(plateau, fantome, pos):
    """pose un fantome en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        fantome (str): la lettre représentant le fantome
        pos (tuple): une paire (lig,col) de deux int
    """
    case.poser_fantome(get_case(plateau, pos), fantome)

def poser_objet(plateau, objet, pos):
    """Pose un objet en position pos sur le plateau. Si cette case contenait déjà
        un objet ce dernier disparait

    Args:
        plateau (dict): le plateau considéré
        objet (int): un entier représentant l'objet. const.AUCUN indique aucun objet
        pos (tuple): une paire (lig,col) de deux int
    """
    case.poser_objet(get_case(plateau, pos), objet)

def plateau_from_str(la_chaine, complet=True):
    """Construit un plateau à partir d'une chaine de caractère contenant les informations
        sur le contenu du plateau (voir sujet)

    Args:
        la_chaine (str): la chaine de caractères décrivant le plateau

    Returns:
        dict: le plateau correspondant à la chaine. None si l'opération a échoué
    """
    return Plateau(la_chaine)

def Plateau(plan):
    """Créer un plateau en respectant le plan donné en paramètre.
        Le plan est une chaine de caractères contenant
            '#' (mur)
            ' ' (couloir non peint)
            une lettre majuscule (un couloir peint par le joueur représenté par la lettre)

    Args:
        plan (str): le plan sous la forme d'une chaine de caractères

    Returns:
        dict: Le plateau correspondant au plan
    """
    plateau = {}
    nb_lignes = 0
    nb_colonnes = 0
    matrice = []
    i = 0

    for line in plan.split('\n'):
        if i == 0:
            nb_lignes = int(line.split(';')[0])
            nb_colonnes = int(line.split(';')[1])
        elif i > 0 and i <= nb_lignes:
            mat_ligne = []
            for j in range(nb_colonnes):
                carac = line[j]
                if carac == '#':
                    mat_ligne.append(case.Case(True))
                elif carac in const.LES_OBJETS:
                    mat_ligne.append(case.Case(False, carac))
                else:
                    mat_ligne.append(case.Case(False))
            matrice.append(mat_ligne)
        
        elif i == nb_lignes + 1:
            plateau["carte"] = matrice # itération de la carte terminée
            plateau['nb_pacmans'] = int(line)

        elif i > nb_lignes + 1 and i <= nb_lignes + 1 + plateau['nb_pacmans']:
            pac = line.split(';')
            pos = (int(pac[1]), int(pac[2]))
            poser_pacman(plateau, pac[0], pos)
        elif i == nb_lignes + 2 + plateau['nb_pacmans']:
            plateau['nb_fantomes'] = int(line)
        elif i > nb_lignes + 2 + plateau['nb_pacmans'] and i <= nb_lignes + 2 + plateau['nb_pacmans'] + plateau['nb_fantomes']:
            fan = line.split(';')
            pos = (int(fan[1]), int(fan[2]))
            poser_fantome(plateau, fan[0], pos)
        i += 1
    
    plateau["lig"] = nb_lignes
    plateau["col"] = nb_colonnes

    return plateau


def set_case(plateau, pos, une_case):
    """remplace la case qui se trouve en position pos du plateau par une_case

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire (lig,col) de deux int
        une_case (dict): la nouvelle case
    """
    (pos_lig, pos_col) = pos
    plateau['carte'][pos_lig][pos_col] = une_case


def enlever_pacman(plateau, pacman, pos):
    """enlève un joueur qui se trouve en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        pacman (str): la lettre représentant le joueur
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        bool: True si l'opération s'est bien déroulée, False sinon
    """
    return case.prendre_pacman(get_case(plateau, pos), pacman)


def enlever_fantome(plateau, fantome, pos):
    """enlève un fantome qui se trouve en position pos sur le plateau

    Args:
        plateau (dict): le plateau considéré
        fantome (str): la lettre représentant le fantome
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        bool: True si l'opération s'est bien déroulée, False sinon
    """
    return case.prendre_fantome(get_case(plateau, pos), fantome)


def prendre_objet(plateau, pos):
    """Prend l'objet qui se trouve en position pos du plateau et retourne l'entier
        représentant cet objet. const.AUCUN indique qu'aucun objet se trouve sur case

    Args:
        plateau (dict): Le plateau considéré
        pos (tuple): une paire (lig,col) de deux int

    Returns:
        int: l'entier représentant l'objet qui se trouvait sur la case.
        const.AUCUN indique aucun objet
    """
    return case.prendre_objet(get_case(plateau, pos))

        
def deplacer_pacman(plateau, pacman, pos, direction, passemuraille=False):
    """Déplace dans la direction indiquée un joueur se trouvant en position pos
        sur le plateau si c'est possible

    Args:
        plateau (dict): Le plateau considéré
        pacman (str): La lettre identifiant le pacman à déplacer
        pos (tuple): une paire (lig,col) d'int
        direction (str): une lettre parmie NSEO indiquant la direction du déplacement
        passemuraille (bool): un booléen indiquant si le pacman est passemuraille ou non

    Returns:
        (int,int): une paire (lig,col) indiquant la position d'arrivée du pacman 
                   (None si le pacman n'a pas pu se déplacer)
    """
    nouvelle_position = pos_arrivee(plateau, pos, direction) 
    position = get_case(plateau,pos)
    if not case.est_mur(position) : 
        if nouvelle_position is not None:
            case_nouvelle_position = get_case(plateau,nouvelle_position)
            if passemuraille or not case.est_mur(case_nouvelle_position):
                poser_pacman(plateau,pacman,nouvelle_position)
                enlever_pacman(plateau,pacman,pos)
                return nouvelle_position
    return None

    
    

def deplacer_fantome(plateau, fantome, pos, direction):
    """Déplace dans la direction indiquée un fantome se trouvant en position pos
        sur le plateau

    Args:
        plateau (dict): Le plateau considéré
        fantome (str): La lettre identifiant le fantome à déplacer
        pos (tuple): une paire (lig,col) d'int
        direction (str): une lettre parmie NSEO indiquant la direction du déplacement

    Returns:
        (int,int): une paire (lig,col) indiquant la position d'arrivée du fantome
                   None si le joueur n'a pas pu se déplacer
    """
    nouvelle_position = pos_arrivee(plateau, pos, direction) 
    
    if nouvelle_position is not None:
        case_nouvelle_position = get_case(plateau,nouvelle_position)
        if not case.est_mur(case_nouvelle_position):
            poser_fantome(plateau,fantome,nouvelle_position)
            enlever_fantome(plateau,fantome,pos)
            return nouvelle_position
    return None

def case_vide(plateau):
    """choisi aléatoirement sur la plateau une case qui n'est pas un mur et qui
       ne contient ni pacman ni fantome ni objet

    Args:
        plateau (dict): le plateau

    Returns:
        (int,int): la position choisie
    """
    cases_vides = []
    for i in range(plateau['lig']):
        for j in range(plateau['col']):
            la_case = get_case(plateau, (i, j))
            if not case.est_mur(la_case) and case.get_objet(la_case) == ' ' and case.get_pacmans(la_case) == set() and case.get_fantomes(la_case) == set():
                cases_vides.append((i, j))
    if cases_vides == []:
        return None
    random.shuffle(cases_vides)
    return cases_vides[0]

def directions_possibles(plateau,pos,passemuraille=False):
    """ retourne les directions vers où il est possible de se déplacer à partir
        de la position pos

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): un couple d'entiers (ligne,colonne) indiquant la position de départ
        passemuraille (bool): indique si on s'autorise à passer au travers des murs
    
    Returns:
        str: une chaine de caractères indiquant les directions possibles
              à partir de pos
    """
    nord = pos_arrivee(plateau, pos, 'N')
    sud = pos_arrivee(plateau, pos, 'S')
    est = pos_arrivee(plateau, pos, 'E')
    ouest = pos_arrivee(plateau, pos, 'O')
    directions = ''
    if passemuraille:
        return 'NSEO'
    if nord != None and not case.est_mur(get_case(plateau, nord)):
        directions += 'N'
    if sud != None and not case.est_mur(get_case(plateau, sud)):
        directions += 'S'
    if est != None and not case.est_mur(get_case(plateau, est)):
        directions += 'E'
    if ouest != None and not case.est_mur(get_case(plateau, ouest)):
        directions += 'O'
    return directions


#---------------------------------------------------------#


def mat_set_val(matrice, lig, col, val):
    """modifie la valeur de la case (lig,col) de la matrice avec la valeur val

    Args:
        matrice (matrice): une matrice
        lig (int): un entier indiquant le numéro de ligne
        col (int): un entier indiquant le numéro de colonne
        val (int): un entier indiquant la valeur à mettre dans la case
    """
    matrice[lig][col] = val


def analyse_plateau(plateau, pos, direction, distance_max):
    """calcul les distances entre la position pos et les différents objets et
        joueurs du plateau si on commence par partir dans la direction indiquée
        en se limitant à la distance max. Si il n'est pas possible d'aller dans la
        direction indiquée à partir de pos, la fonction doit retourner None

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers indiquant la postion de calcul des distances
        distance_max (int): un entier indiquant la distance limite de la recherche
    Returns:
        dict: un dictionnaire de listes. 
                Les clés du dictionnaire sont 'objets', 'pacmans' et 'fantomes'
                Les valeurs du dictionnaire sont des listes de paires de la forme
                    (dist,ident) où dist est la distance de l'objet, du pacman ou du fantome
                                    et ident est l'identifiant de l'objet, du pacman ou du fantome
            S'il n'est pas possible d'aller dans la direction indiquée à partir de pos
            la fonction retourne None
    """
    nb_lignes = get_nb_lignes(plateau)
    nb_colonnes = get_nb_colonnes(plateau)
    calque = [[None for _ in range(nb_colonnes)] for _ in range(nb_lignes)]
    
    distances = {'objets': [], 'pacmans': [], 'fantomes': []}

    possibilite_directions = directions_possibles(plateau, pos)

    if direction not in possibilite_directions:
        return None

    pos = pos_arrivee(plateau, pos, direction)
    la_case = get_case(plateau, pos)
    objet = case.get_objet(la_case)
    fantome = case.get_fantomes(la_case)
    pacman = case.get_pacmans(la_case)
    if objet != const.AUCUN:
        distances['objets'].append((1, objet))
    elif fantome != set():
        fantome = ', '.join(fantome) #transforme le set en chaine de caractères
        distances['fantomes'].append((1, fantome))
    elif pacman != set():
        pacman = ', '.join(pacman)
        distances['pacmans'].append((1, pacman))


    mat_set_val(calque, pos[0], pos[1], 1)
    arret = False
    while not arret:
        arret = True
        for lig in range(nb_lignes):
            for col in range(nb_colonnes):
                pos = (lig, col)
                la_case = get_case(plateau, pos)
                if not case.est_mur(la_case):
                    if calque[lig][col] is None:
                        for dir in directions_possibles(plateau, pos):
                            voisin = pos_arrivee(plateau, pos, dir)
                            calque_case_voisine = calque[voisin[0]][voisin[1]]
                            if calque_case_voisine is not None:
                                if calque_case_voisine < distance_max:
                                    dist = calque_case_voisine + 1
                                    mat_set_val(calque, lig, col, dist)
                                    objet = case.get_objet(la_case)
                                    fantome = case.get_fantomes(la_case)
                                    
                                    pacman = case.get_pacmans(la_case)
                                    
                                    if objet != const.AUCUN:
                                        distances['objets'].append((dist, objet))
                                    if fantome != set():
                                        fantome = ', '.join(fantome)
                                        distances['fantomes'].append((dist, fantome))
                                    if pacman != set():
                                        pacman = ', '.join(pacman)
                                        distances['pacmans'].append((dist, pacman))
                                    arret = False
    return distances
    
pl = Plateau(open("./cartes/test3.txt").read())
print(analyse_plateau(pl, (5,5), 'N', get_nb_colonnes(pl) * get_nb_lignes(pl)))
print(analyse_plateau(pl, (5,5), 'E', get_nb_colonnes(pl) * get_nb_lignes(pl)))
print(analyse_plateau(pl, (5,5), 'O', get_nb_colonnes(pl) * get_nb_lignes(pl)))
print(analyse_plateau(pl, (5,5), 'S', get_nb_colonnes(pl) * get_nb_lignes(pl)))

def intersection(direction):
    """
    calcule la direction perpendiculaire à la direction indiquée
    Args:
        direction (str): la direction choisie
    Returns:
        str: la direction perpendiculaire
    """
    if direction == 'N' or direction == 'S':
        return 'EO'
    if direction == 'E' or direction == 'O':
        return 'NS'

    
def opposite(direction):
    """
    calcule la direction opposée à la direction indiquée
    Args:
        direction (str): la direction choisie
    Returns:
        str: la direction opposée
    """
    if direction == 'N':
        return 'S'
    if direction == 'S':
        return 'N'
    if direction == 'E':
        return 'O'
    if direction == 'O':
        return 'E'
    
def prochaine_intersection(plateau,pos,direction):
    """calcule la distance de la prochaine intersection
        si on s'engage dans la direction indiquée

    Args:
        plateau (dict): le plateau considéré
        pos (tuple): une paire d'entiers donnant la position de départ
        direction (str): la direction choisie

    Returns:
        int: un entier indiquant la distance à la prochaine intersection
             -1 si la direction mène à un cul de sac.
    """
    bloque = False
    dist = 0
    while not bloque:
        arrive_pos = pos_arrivee(plateau, pos, direction)
        possibilite_directions = directions_possibles(plateau, arrive_pos)
        #print(dist, ": arrive_pos", arrive_pos, "direction", direction, "possibilite_directions", possibilite_directions)
        if intersection(direction) in possibilite_directions:
            return dist
            #print("intersection en dist", dist)
        if direction not in possibilite_directions or arrive_pos == None:
            possibilite_directions = possibilite_directions.replace(opposite(direction), '') #Si le chemin tourne, on recupère la direction en retirant le chemin opposé
            if len(possibilite_directions) == 1:
                #print("changement de direction", direction,"->", possibilite_directions)
                direction = possibilite_directions
            else:
                bloque = True
        
        dist += 1
        pos = arrive_pos
    if bloque:
        return -1
    return dist

# A NE PAS DEMANDER
def plateau_2_str(plateau):
        res = str(get_nb_lignes(plateau))+";"+str(get_nb_colonnes(plateau))+"\n"
        pacmans = []
        fantomes = []
        for lig in range(get_nb_lignes(plateau)):
            ligne = ""
            for col in range(get_nb_colonnes(plateau)):
                la_case = get_case(plateau,(lig, col))
                if case.est_mur(la_case):
                    ligne += "#"
                    les_pacmans = case.get_pacmans(la_case)
                    for pac in les_pacmans:
                        pacmans.append((pac, lig, col))
                else:
                    obj = case.get_objet(la_case)
                    les_pacmans = case.get_pacmans(la_case)
                    les_fantomes= case.get_fantomes(la_case)
                    ligne += str(obj)
                    for pac in les_pacmans:
                        pacmans.append((pac, lig, col))
                    for fantome in les_fantomes:
                        fantomes.append((fantome,lig,col))
            res += ligne+"\n"
        res += str(len(pacmans))+'\n'
        for pac, lig, col in pacmans:
            res += str(pac)+";"+str(lig)+";"+str(col)+"\n"
        res += str(len(fantomes))+"\n"
        for fantome, lig, col in fantomes:
            res += str(fantome)+";"+str(lig)+";"+str(col)+"\n"
        return res

