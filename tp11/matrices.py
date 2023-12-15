
matrice1 = [[10,11,12,13],[14,15,16,17],[18,19,20,21]]
matrice2 = [['A','B','C'],['D','E','F']]
matrice3 = [[2,7,6],[9,5,1],[4,3,8]]


def construit_matrice(nb_lignes, nb_colonnes, valeur_par_defaut=0):
    return [[valeur_par_defaut for _ in range(nb_colonnes)] for _ in range(nb_lignes)]

def get_nb_lignes(matrice):
    return len(matrice)

def get_nb_colonnes(matrice):
    return len(matrice[0])

def get_val(matrice, ligne, colonne):
    return matrice[ligne][colonne]

def set_val(matrice, ligne, colonne, nouvelle_valeur):
    matrice[ligne][colonne] = nouvelle_valeur

def get_ligne(matrice, ligne):
    return matrice[ligne]

def get_colonne(matrice, colonne):
    col = []
    for ligne in matrice:
        col.append(ligne[colonne])
    return col

def get_diagonale_principale(matrice):
    ligne = 0
    colonne = 0
    diagonale = []
    while get_nb_lignes(diagonale) < get_nb_lignes(matrice):
        diagonale.append(get_val(matrice, ligne, colonne))
        ligne += 1
        colonne += 1
    return diagonale

def get_diagonale_secondaire(matrice):
    ligne = 0
    colonne = get_nb_colonnes(matrice)-1
    diagonale = []
    while get_nb_lignes(diagonale) < get_nb_lignes(matrice):
        diagonale.append(get_val(matrice, ligne, colonne))
        ligne += 1
        colonne -= 1
    return diagonale

def transposee(matrice):
    transpose = []
    for i in range(get_nb_colonnes(matrice)):
        transpose.append(get_colonne(matrice, i))
    return transpose

def is_triangulaire_inf(matrice):
    i = 1
    for ligne in range(get_nb_lignes(matrice)):
        for elem in get_ligne(matrice, ligne)[i:]:
            i += 1
            if elem != 0:
                return False
    return True

def is_triangulaire_sup(matrice):
    i = 1
    for ligne in range(1, get_nb_lignes(matrice)):
        for elem in get_ligne(matrice, ligne)[:i]:
            i += 1
            if elem != 0:
                return False
    return True

def bloc(matrice, ligne, colonne, hauteur, largeur):
    matrice_bloc = []
    if ligne < 0 or colonne < 0 or ligne + hauteur > get_nb_lignes(matrice) or colonne + largeur > get_nb_colonnes(matrice): 
        return None
    for i in range(ligne, ligne + hauteur):
        ligne_matrice_bloc = []
        for j in range(colonne, colonne + largeur):
            ligne_matrice_bloc.append(get_val(matrice, i, j))
        matrice_bloc.append(ligne_matrice_bloc)
    return matrice_bloc

def somme(matrice1, matrice2):
    matrice_somme = [[0 for _ in range(get_nb_colonnes(matrice2))] for _ in range(get_nb_lignes(matrice1))]
    if (get_nb_lignes(matrice1) != get_nb_lignes(matrice2)) or (get_nb_colonnes(matrice1) != get_nb_colonnes(matrice2)):
        return None
    for ligne in range(get_nb_lignes(matrice_somme)):
        for colonne in range(get_nb_colonnes(matrice_somme)):
            somme = get_val(matrice1, ligne, colonne) + get_val(matrice2, ligne, colonne)
            set_val(matrice_somme, ligne, colonne, somme)
    return matrice_somme

def produit(matrice1, matrice2):
    matrice_produit = [[0 for _ in range(get_nb_colonnes(matrice2))] for _ in range(get_nb_lignes(matrice1))]
    for ligne in range(get_nb_lignes(matrice1)):
        for colonne in range(get_nb_colonnes(matrice2)):
            produit = 0
            for k in range(get_nb_lignes(matrice2)):
                produit += get_val(matrice1, ligne, k) * get_val(matrice2, k, colonne)
            set_val(matrice_produit, ligne, colonne, produit)
    return matrice_produit

def colle_sous_matrice(matrice, sous_matrice, ligne, colonne):
    ligne_sous_matrice = 0
    for ligne_matrice in range(ligne, get_nb_lignes(sous_matrice) + ligne):
        colonne_sous_matrice = 0
        for colonne_matrice in range(colonne, get_nb_colonnes(sous_matrice)):
            set_val(matrice, ligne_matrice, colonne_matrice, get_val(sous_matrice, ligne_sous_matrice, colonne_sous_matrice))
            colonne_sous_matrice += 1
        ligne_sous_matrice += 1
    return matrice

