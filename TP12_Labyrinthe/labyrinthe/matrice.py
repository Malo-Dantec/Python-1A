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
    ...

def get_nb_lignes(matrice):
    """renvoie le nombre de lignes de la matrice

    Args:
        matrice (matrice): une matrice selon la modélisation précisée
        dans la documentation du module

    Returns:
        int: le nombre de lignes de la matrice
    """
    ...

def get_nb_colonnes(matrice):
    """renvoie le nombre de colonnes de la matrice

    Args:
        matrice (matrice): une matrice selon la modélisation précisée
        dans la documentation du module

    Returns:
        int: le nombre de colonnes de la matrice
    """
    ...

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
    ...

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
    ...

def affiche(matrice):
    """Affiche la matrice sur la sortie standard

    Args:
        matrice (matrice): une matrice selon la modélisation précisée
        dans la documentation du module
    Returns:
        None
    """
    ...

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
