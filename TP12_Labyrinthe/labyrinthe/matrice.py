"""
Une implémentation des matrices 2D en python
Détailler ici la modélisation choisie en donnant au moins un exemple
"""

def new_matrice(nb_lignes, nb_colonnes, valeur_par_defaut=0):
    """Construit et une nouvelle matrice

    Args:
        nb_lignes (int): le nombre de lignes de la matrice
        nb_colonnes (int): le nombre de colonnes de la matrice
        valeur_par_defaut (int, optional): la valeur qui sera dans chacune des case de la matrice.
        Defaults to 0.

    Returns:
        matrice: une matrice dont le nombre de lignes est nb_lignes, le nombre de colonnes
                 est nb_colonnes
        et dont toutes les valeurs sont à valeur_par_defaut
    """
    matrice = {}
    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):
            matrice[ligne, colonne] = valeur_par_defaut
    return nb_lignes, nb_colonnes, matrice



def get_nb_lignes(matrice):
    """renvoie le nombre de lignes de la matrice

    Args:
        matrice (matrice): une matrice selon la modélisation précisée
        dans la documentation du module

    Returns:
        int: le nombre de lignes de la matrice
    """
    return matrice[0]

def get_nb_colonnes(matrice):
    """renvoie le nombre de colonnes de la matrice

    Args:
        matrice (matrice): une matrice selon la modélisation précisée
        dans la documentation du module

    Returns:
        int: le nombre de colonnes de la matrice
    """
    return matrice[1]

def get_val(matrice, ligne, colonne):
    """renvoie une valeur de la matrice

    Args:
        matrice (matrice): une matrice selon la modélisation précisée
        dans la documentation du module
        ligne (int): le numéro de la ligne (on commence à 0)
        colonne (int): le numéro de la colonne (on commence à 0)
    Returns:
        variable: le contenu de la case de la matrice qui se trouve à la ligne
        numéro ligne et à la colonne numéro colonne
    """
    return matrice[2][ligne, colonne]



def set_val(matrice, ligne, colonne, new_val):
    """modifie le contenu de la case de la matrice qui se trouve à la ligne
        numéro ligne et à la colonne numéro colonne en y mettant la valeur
        new_val
    Args:
        matrice (matrice): une matrice selon la modélisation précisée
        dans la documentation du module
        ligne (int): le numéro de la ligne (on commence à 0)
        colonne (int): le numéro de la colonne (on commence à 0)
    Returns:
        None
    """
    matrice[2][ligne, colonne] = new_val


def affiche(matrice):
    """Affiche la matrice sur la sortie standard

    Args:
        matrice (matrice): une matrice selon la modélisation précisée
        dans la documentation du module
    Returns:
        None
    """
    for ligne in range(get_nb_lignes(matrice)):
        for colonne in range(get_nb_colonnes(matrice)):
            if get_val(matrice, ligne, colonne) != None:
                if colonne != get_nb_colonnes(matrice)-1:
                    print(get_val(matrice, ligne, colonne), end=',')
                else:
                    print(get_val(matrice, ligne, colonne), end='')
            else:
                if colonne != get_nb_colonnes(matrice)-1:
                    print('', end=',')
                else:
                    print('', end='')
        print()

        

#-----------------------------------------
# entrées sorties dans des fichiers
#-----------------------------------------

def sauve_matrice(matrice, nom_fichier):
    """Sauvegarde la matrice dans un fichier csv dont chaque ligne
    représente une ligne de la matrice et les valeurs sont spérarées
    par des virgules (',')

    Args:
        matrice (matrice): une matrice selon la modélisation précisée
        dans la documentation du module
        nom_fichier (str): le nom d'un chemin vers un fichier
                           par exemple "./matrice1.csv" ou "../sauvegardes/matrice3.csv"
    Returns:
        None
    """
    fichier = open(nom_fichier, 'w')
    for no_ligne in range(get_nb_lignes(matrice)):
        ligne = ''
        for no_colonne in range(get_nb_colonnes(matrice)):
            valeur = get_val(matrice, no_ligne, no_colonne)
            if valeur is None:
                ligne += ','
            else:
                ligne += str(valeur) + ','
        ligne = ligne[:-1]+'\n'
        fichier.write(ligne)
    fichier.close()
sauve_matrice((9, 9, {(0, 0): 6, (0, 1): None, (0, 2): None, (0, 3): None, (0, 4): None, (0, 5): None, (0, 6): None, (0, 7): None, (0, 8): None, (1, 0): 5, (1, 1): 4, (1, 2): 3, (1, 3): None, (1, 4): None, (1, 5): None, (1, 6): None, (1, 7): None, (1, 8): None, (2, 0): None, (2, 1): None, (2, 2): 2, (2, 3): None, (2, 4): 4, (2, 5): 5, (2, 6): 6, (2, 7): 7, (2, 8): None, (3, 0): None, (3, 1): None, (3, 2): 1, (3, 3): None, (3, 4): 3, (3, 5): None, (3, 6): None, (3, 7): 6, (3, 8): None, (4, 0): None, (4, 1): None, (4, 2): 0, (4, 3): 1, (4, 4): 2, (4, 5): 3, (4, 6): 4, (4, 7): 5, (4, 8): None, (5, 0): None, (5, 1): None, (5, 2): None, (5, 3): 2, (5, 4): None, (5, 5): None, (5, 6): None, (5, 7): 6, (5, 8): None, (6, 0): None, (6, 1): None, (6, 2): None, (6, 3): 3, (6, 4): None, (6, 5): None, (6, 6): None, (6, 7): 7, (6, 8): None, (7, 0): None, (7, 1): None, (7, 2): None, (7, 3): 4, (7, 4): 5, (7, 5): 6, (7, 6): 7, (7, 7): 8, (7, 8): None, (8, 0): None, (8, 1): None, (8, 2): None, (8, 3): None, (8, 4): None, (8, 5): None, (8, 6): None, (8, 7): 9, (8, 8): 10}), 'Chemin_le_plus_court1')

def lignes_et_colonnes(nom_fichier):
    """renvoie un tuple contenant le nombre de lignes et le nombre de colonnes d'une matrice
       dans un fichier csv

    Args:
        nom_fichier (str): le nom d'un chemin vers un fichier
                           par exemple "./matrice1.csv" ou "../sauvegardes/matrice3.csv"
    Returns:
        tuple: un tuple de deux nombres entiers (nombre_de_lignes, nombre_de_colonnes) de la matrice
               contenu dans le fichier
    """
    fichier = open(nom_fichier, 'r')
    nb_lignes = 0
    for ligne in fichier:
        nb_lignes += 1
    nb_colonnes  = len(ligne.split(","))
    return (nb_lignes, nb_colonnes)
    
def charge_matrice(nom_fichier, type_valeur='int'):
    """Charge une matrice à partir d'un fichier csv dont chaque ligne
    représente une ligne de la matrice et les valeurs (des entiers ou des str)
    sont séparées par des virgules (',')

    Args:
        nom_fichier (str): le nom d'un chemin vers un fichier
                           par exemple "./matrice1.csv" ou "../sauvegardes/matrice3.csv"
        type_valeur (str, optional): le type des valeurs ('int' ou 'str'. Defaults to 'int'.
    Returns:
        matrice (matrice): une matrice selon la modélisation précisée
        dans la documentation du module
    """
    (nb_lignes, nb_colonnes) = lignes_et_colonnes(nom_fichier)
    ma_matrice = new_matrice(nb_lignes, nb_colonnes, None)
    fichier = open(nom_fichier, 'r')
    no_ligne = 0
    for ligne in fichier:
        liste_des_valeurs = ligne[:-1].split(",")
        no_colonne = 0
        for valeur in liste_des_valeurs:
            if valeur == '':
                valeur = None
            elif type_valeur == 'int':
                valeur = int(valeur)
            else:
                valeur = valeur
            set_val(ma_matrice, no_ligne, no_colonne, valeur)                
            no_colonne += 1
        no_ligne += 1
    return ma_matrice
