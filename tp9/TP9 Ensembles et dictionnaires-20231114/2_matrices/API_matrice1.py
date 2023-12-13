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
    nb_valeur = nb_colonnes*nb_lignes
    return (nb_lignes,nb_colonnes,[valeur_par_defaut]*nb_valeur)



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
    matrice[2][ligne*get_nb_colonnes(matrice)+colonne] = nouvelle_valeur


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
    return matrice[2][ligne*get_nb_colonnes(matrice)+colonne]

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
    nbligne=0
    nbcolonne=0
    valeur=[]
    res=()
    fic=open(nom_fichier,'r')
    for ligne in fic:
        nbligne+=1
        l_champs=ligne.split(',')[:-1]
        valeur+=l_champs
    nbcolonne=len(l_champs)
    res=(nbligne,nbcolonne,valeur)
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
    nbcolonne=1
    fic=open(nom_fichier,"w")
    for nb in matrice[2]:
        if nbcolonne<matrice[1]:
            fic.write(str(nb)+',')
            nbcolonne+=1
        elif nbcolonne==matrice[1]:
            fic.write(str(nb)+','+'\n')
            nbcolonne=1
    fic.close()
    return None

def get_ligne(matrice, ligne):
    val = []
    nbcolonne = matrice[1]
    i = nbcolonne*(ligne-1)
    while i < nbcolonne*ligne:
        val.append(matrice[2][i])
        i+=1
    return val

def get_colonne(matrice, colonne):
    val = []
    i = colonne-1
    while i < len(matrice[2]):
        val.append(matrice[2][i])
        i+=matrice[1]
    return val

def get_diagonale_principale(matrice):
    val = []
    i = 0
    while i < len(matrice[2]):
        val.append(matrice[2][i])
        i+=matrice[1]+1
    return val

def get_diagonale_secondaire(matrice):
    val = []
    i = matrice[1]-1
    while i < len(matrice[2]):
        if len(val) > matrice[0]-1:
            break
        val.append(matrice[2][i])
        i+=matrice[1]-1
    return val

def transposee(matrice):
    val = []
    i = 1
    while len(val) < len(matrice[2]):
        res = get_colonne(matrice, i)
        for elem in res:
            val.append(elem)
        i += 1
    return matrice[1], matrice[0], val

def is_triangulaire_inf(matrice):
    for i in range(matrice[0]):
        for j in range(i + 1, matrice[1]):
            if matrice[2][j] != 0:
                return False
    return True

def bloc(matrice, ligne, colonne, hauteur, largeur):
    liste_bloc = []
    max_ligne = min(ligne + hauteur, matrice[0])
    max_colonne = min(colonne + largeur, matrice[1])
    for i in range(ligne, max_ligne):
        for j in range(colonne, max_colonne):
            k = i * matrice[1] + j
            liste_bloc.append(matrice[2][k])
    return hauteur, largeur, liste_bloc
