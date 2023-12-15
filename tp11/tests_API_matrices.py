""" tests pour les API matrices 
    Remarques : tous les tests de ce fichier doivent passer quelle que soit l'API utilisée
    """
import matrices as API

def matrice1():
    m1 = API.construit_matrice(3, 4, None)
    API.set_val(m1, 0, 0, 10)
    API.set_val(m1, 0, 1, 11)    
    API.set_val(m1, 0, 2, 12)
    API.set_val(m1, 0, 3, 13)
    API.set_val(m1, 1, 0, 14)
    API.set_val(m1, 1, 1, 15)
    API.set_val(m1, 1, 2, 16)
    API.set_val(m1, 1, 3, 17)
    API.set_val(m1, 2, 0, 18)
    API.set_val(m1, 2, 1, 19)
    API.set_val(m1, 2, 2, 20)
    API.set_val(m1, 2, 3, 21)
    return m1

def matrice2():
    m2 = API.construit_matrice(2, 3, None)
    print(m2)
    API.set_val(m2, 0, 0, 'A')
    API.set_val(m2, 0, 1, 'B')    
    API.set_val(m2, 0, 2, 'C')
    API.set_val(m2, 1, 0, 'D')
    API.set_val(m2, 1, 1, 'E')
    API.set_val(m2, 1, 2, 'F')
    return m2

def matrice3():
    m3 = API.construit_matrice(3, 3, None)
    API.set_val(m3, 0, 0, 2)
    API.set_val(m3, 0, 1, 7)    
    API.set_val(m3, 0, 2, 6)
    API.set_val(m3, 1, 0, 9)
    API.set_val(m3, 1, 1, 5)
    API.set_val(m3, 1, 2, 1)
    API.set_val(m3, 2, 0, 4)
    API.set_val(m3, 2, 1, 3)
    API.set_val(m3, 2, 2, 8)
    return m3

def test_get_nb_lignes():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert API.get_nb_lignes(m1) == 3
    assert API.get_nb_lignes(m2) == 2
    assert API.get_nb_lignes(m3) == 3
        
def test_get_nb_colonnes():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert API.get_nb_colonnes(m1) == 4
    assert API.get_nb_colonnes(m2) == 3
    assert API.get_nb_colonnes(m3) == 3

def test_get_val():
    m1 = matrice1()
    m2 = matrice2()
    m3 = matrice3()
    assert API.get_val(m1, 0, 1) == 11
    assert API.get_val(m1, 2, 1) == 19
    assert API.get_val(m2, 1, 1) == 'E'
    assert API.get_val(m2, 0, 2) == 'C'
    assert API.get_val(m3, 2, 0) == 4
    assert API.get_val(m3, 1, 0) == 9

def test_get_ligne():
    m1 = matrice1()
    m3 = matrice3()
    assert API.get_ligne(m1,1) == [14, 15, 16, 17]
    assert API.get_ligne(m3,2) == [4, 3, 8]

def test_get_colonne():
    m1 = matrice1()
    m3 = matrice3()
    assert API.get_colonne(m1,1) == [11, 15, 19]
    assert API.get_colonne(m3,2) == [6, 1, 8]

def test_get_diagonale_principale():
    m3 = matrice3()
    assert API.get_diagonale_principale(m3) == [2,5,8]

def test_get_diagonale_secondaire():
    m3 = matrice3()
    assert API.get_diagonale_secondaire(m3) == [6,5,4]

def test_transposee():
    m3 = matrice3()
    m2 = matrice2()
    assert API.transposee(m3) == ([[2,9,4],[7,5,3],[6,1,8]])
    assert API.transposee(m2) == ([['A','D'],['B','E'],['C','F']])

def test_is_triangulaire_inf():
    m3 = matrice3()
    m2 = matrice2()
    assert not API.is_triangulaire_inf(m2)
    assert not API.is_triangulaire_inf(m3)
    assert API.is_triangulaire_inf([[1, 0, 0], [2, 2, 0], [3, 3, 3]])

def test_is_triangulaire_sup():
    m3 = matrice3()
    m2 = matrice2()
    assert not API.is_triangulaire_sup(m2)
    assert not API.is_triangulaire_sup(m3)
    assert API.is_triangulaire_sup([[1, 1, 1], [0, 2, 2], [0, 0, 3]])

def test_bloc():
    m3 = matrice3()
    assert API.bloc(m3, 0, 0, 2, 2) == [[2, 7], [9, 5]]
    assert API.bloc(m3, 1, 1, 2, 2) == [[5, 1], [3, 8]]
    assert API.bloc(m3, 1, 1, 5, 5) is None

def test_somme():
    assert API.somme([[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[9, 10, 11], [12, 13, 14], [15, 16, 17]]) == [[9, 11, 13], [15, 17, 19], [21, 23, 25]]
    assert API.somme([[1, 2, 3]], [[1, 2]]) is None
    assert API.somme([[1, 2, 3]], [[4, 5, 6]]) == [[5, 7, 9]]

def test_produit():
    assert API.produit([[2,7,6],[9,5,1],[4,3,8]], [[2,2,2],[2,2,2],[2,3,2]]) == [[30, 36, 30], [30, 31, 30], [30, 38, 30]]
    assert API.produit([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, -1], [-2, -3]]) == [[19, -3], [61, 9]]
    assert API.produit([[1, 2], [3, 4], [5, 6], [7, 8]], [[1, 2, 3], [4, 5, 6]]) == [[9, 12, 15], [19, 26, 33], [29, 40, 51], [39, 54, 69]]

def test_colle():
    assert API.colle_sous_matrice([[1, 2, 3],[4, 5, 6],[7, 8, 9]], [[67, 42], [43, 17]], 0, 0) == [[67, 42, 3], [43, 17, 6], [7, 8, 9]]
    assert API.colle_sous_matrice([[1, 2, 3],[4, 5, 6],[7, 8, 9]], [[67, 42], [43, 17]], 0, 0) == [[67, 42, 3], [43, 17, 6], [7, 8, 9]]
    assert API.colle_sous_matrice([[1, 2, 3],[4, 5, 6],[7, 8, 9]], [[6, 5, 4], []], 1, 0) == [[1, 2, 3], [6, 5, 4], [7, 8, 9]]
    