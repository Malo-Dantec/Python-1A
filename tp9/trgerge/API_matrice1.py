""" Matrices : API n 1 """


def construit_matrice(nb_lignes, nb_colonnes, valeur_par_defaut):
    """crée une nouvelle matrice en mettant la valeur par défaut dans chacune de ses cases.

    Args:
        nb_lignes (int): le nombre de lignes de la matrice
        nb_colonnes (int): le nombre de colonnes de la matrice
        valeur_par_defaut : La valeur que prendra chacun des éléments de la matrice

    Returns:
        une nouvelle matrice qui contient la valeur par défaut dans chacune de ses cases
    """
    nb_element=nb_lignes*nb_colonnes
    return (nb_lignes, nb_colonnes,[valeur_par_defaut]*nb_element)



def set_val(matrice, ligne, colonne, nouvelle_valeur):
    """permet de modifier la valeur de l'élément qui se trouve à la ligne et à la colonne
    spécifiées. Cet élément prend alors la valeur nouvelle_valeur

    Args:
        matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)
        nouvelle_valeur : la nouvelle valeur que l'on veut mettre dans la case

    Returns:
        None
    """
    n=get_nb_colonnes(matrice)
    ind= n*ligne+colonne
    matrice[2][ind]=nouvelle_valeur
    return None


def get_nb_lignes(matrice):
    """permet de connaître le nombre de lignes d'une matrice

    Args:
        matrice : une matrice

    Returns:
        int : le nombre de lignes de la matrice
    """
    return matrice[0]


def get_nb_colonnes(matrice):
    """permet de connaître le nombre de colonnes d'une matrice

    Args:
        matrice : une matrice

    Returns:
        int : le nombre de colonnes de la matrice
    """
    return matrice[1]


def get_val(matrice, ligne, colonne):
    """permet de connaître la valeur de l'élément de la matrice dont on connaît
    le numéro de ligne et le numéro de colonne.

    Args:
        matrice : une matrice
        ligne (int) : le numéro d'une ligne (la numérotation commence à zéro)
        colonne (int) : le numéro d'une colonne (la numérotation commence à zéro)

    Returns:
        la valeur qui est dans la case située à la ligne et la colonne spécifiées
    """
    n=get_nb_colonnes(matrice)
    ind= n*ligne+colonne
    return matrice[2][ind]

# Fonctions pour l'affichage 

def affiche_ligne_separatrice(matrice, taille_cellule=4):
    """fonction auxilliaire qui permet d'afficher (dans le terminal)
    une ligne séparatrice

    Args:
        matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    print()
    for _ in range(get_nb_colonnes(matrice) + 1):
        print('-'*taille_cellule+'+', end='')
    print()


def affiche(matrice, taille_cellule=4):
    """permet d'afficher une matrice dans le terminal

    Args:
        matrice : une matrice
        taille_cellule (int, optional): la taille d'une cellule. Defaults to 4.
    """
    nb_colonnes = get_nb_colonnes(matrice)
    nb_lignes = get_nb_lignes(matrice)
    print(' '*taille_cellule+'|', end='')
    for i in range(nb_colonnes):
        print(str(i).center(taille_cellule) + '|', end='')
    affiche_ligne_separatrice(matrice, taille_cellule)
    for i in range(nb_lignes):
        print(str(i).rjust(taille_cellule) + '|', end='')
        for j in range(nb_colonnes):
            print(str(get_val(matrice, i, j)).rjust(taille_cellule) + '|', end='')
        affiche_ligne_separatrice(matrice, taille_cellule)
    print()


# Ajouter ici les fonctions supplémentaires, sans oublier de compléter le fichier
# tests_API_matrice.py avec des fonctions de tests

def charge_matrice_str(nom_fichier):
    """permet créer une matrice de str à partir d'un fichier CSV.

    Args:
        nom_fichier (str): le nom d'un fichier CSV (séparateur  ',')

    Returns:
        une matrice de str
    """
    cptl=0
    cptc=0
    valeur=[]
    res=()
    fic=open(nom_fichier,'r')
    for ligne in fic:
        cptl+=1
        l_champs=ligne.split(',')[:-1]
        valeur+=l_champs
    cptc=len(l_champs)
    res=(cptl,cptc,valeur)
    fic.close()
    return res


def sauve_matrice(matrice, nom_fichier):
    """permet sauvegarder une matrice dans un fichier CSV.
    Attention, avec cette fonction, on perd l'information sur le type des éléments

    Args:
        matrice : une matrice
        nom_fichier (str): le nom du fichier CSV que l'on veut créer (écraser)

    Returns:
        None
    """
    cptc=1
    fic=open(nom_fichier,"w")
    for nb in matrice[2]:
        if cptc<matrice[1]:
            fic.write(str(nb)+',')
            cptc+=1
        elif cptc==matrice[1]:
            fic.write(str(nb)+','+'\n')
            cptc=1
    fic.close()
    return None

def get_ligne(matrice,ligne):
