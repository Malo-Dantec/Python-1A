
matrice1 = [[10,11,12,13],[14,15,16,17],[18,19,20,21]]
matrice2 = [['A','B','C'],['D','E','F']]
matrice3 = [[2,7,6],[9,5,1],[4,3,8]]


def construit_matrice(nb_lignes, nb_colonnes, valeur_par_defaut=0):
    res = []
    for _ in range(0, nb_lignes):
        ligne = []
        for _ in range(0, nb_colonnes):
            ligne.append(valeur_par_defaut)
        res.append(ligne)
    return res

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
    i = 0
    j = 0
    diagonale = []
    while len(diagonale) < len(matrice):
        diagonale.append(matrice[i][j])
        i += 1
        j += 1
    return diagonale

def get_diagonale_secondaire(matrice):
    i = 0
    j = len(matrice[0])-1
    diagonale = []
    while len(diagonale) < len(matrice):
        diagonale.append(matrice[i][j])
        i += 1
        j -= 1
    return diagonale

def transposee(matrice):
    transpose = []
    for i in range(len(matrice[0])):
        transpose.append(get_colonne(matrice, i))
    return transpose

def is_triangulaire_inf(matrice):
    i = 1
    for l in range(0, len(matrice)):
        for elem in get_ligne(matrice, l)[i:]:
            i += 1
            if elem != 0:
                return False
    return True

def is_triangulaire_sup(matrice):
    i = 1
    for l in range(1, len(matrice)):
        for elem in get_ligne(matrice, l)[:i]:
            i += 1
            if elem != 0:
                return False
    return True

def bloc(matrice, ligne, colonne, hauteur, largeur):
    matrice_bloc = []
    if ligne < 0 or colonne < 0 or ligne + hauteur > len(matrice) or colonne + largeur > len(matrice[0]): 
        return None
    for i in range(ligne, ligne + hauteur):
        ligne_matrice_bloc = []
        for j in range(colonne, colonne + largeur):
            ligne_matrice_bloc.append(matrice[i][j])
        matrice_bloc.append(ligne_matrice_bloc)
    return matrice_bloc

def somme(matrice1, matrice2):
    matrice_somme = [[0 for _ in range(len(matrice2[0]))] for _ in range(len(matrice1))]
    if (get_nb_lignes(matrice1) != get_nb_lignes(matrice2)) or (get_nb_colonnes(matrice1) != get_nb_colonnes(matrice2)):
        return None
    for i in range(len(matrice_somme)):
        for j in range(len(matrice_somme[0])):
            res = matrice1[i][j] + matrice2[i][j]
            set_val(matrice_somme, i, j, res)
    return matrice_somme

def produit(matrice1, matrice2):
    matrice_produit = [[0 for _ in range(len(matrice2[0]))] for _ in range(len(matrice1))]
    for i in range(len(matrice1)):
        for j in range(len(matrice2[0])):
            res = 0
            for k in range(len(matrice2)):
                res += matrice1[i][k] * matrice2[k][j]
            set_val(matrice_produit, i, j, res)
    return matrice_produit

