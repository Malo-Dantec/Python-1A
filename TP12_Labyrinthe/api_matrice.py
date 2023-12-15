import random
import csv

def creer_matrice(ligne, colonne):
    """résumé :

    Args:
        ligne (type): 
        colonne (type): 

    Retourne:
        _type_: 
    """    
    matrice = []
    for i in range(ligne):
        ligne_matrice = []
        for j in range(colonne):
            ligne_matrice.append(random.randint(0, 100))
        matrice.append(ligne_matrice)
    return matrice

def get_valeur(matrice, ligne, colonne):
    """résumé :

    Args:
        matrice (type): 
        ligne (type): 
        colonne (type): 

    Retourne:
        _type_: 
    """    
    return matrice[ligne][colonne]

def set_valeur(matrice, ligne, colonne, valeur):
    """résumé :

    Args:
        matrice (type): 
        ligne (type): 
        colonne (type): 
        valeur (type): 
    """    
    matrice[ligne][colonne] = valeur

def get_nombre_de_colonnes(matrice):
    """résumé :

    Args:
        matrice (type): 

    Retourne:
        _type_: 
    """    
    return len(matrice[0]) if matrice else 0

def get_nombre_de_lignes(matrice):
    """résumé :

    Args:
        matrice (type): 

    Retourne:
        _type_: 
    """    
    return len(matrice)


def enregistre_matrice(matrice, nom_fichier):
    """résumé :

    Args:
        matrice (type): 
        nom_fichier (type): 
    """    
    with open(nom_fichier, 'w', newline='') as fichier_csv:
        writer = csv.writer(fichier_csv)
        for ligne in matrice:
            writer.writerow(ligne)

def charge_matrice(nom_fichier):
    """résumé :

    Args:
        nom_fichier (type): 

    Retourne:
        _type_: 
    """    
    matrice_chargee = []
    with open(nom_fichier, 'r') as fichier_csv:
        reader = csv.reader(fichier_csv)
        for ligne in reader:
            ligne_entiers = []
            for valeur in ligne:
                ligne_entiers.append(int(valeur))
            matrice_chargee.append(ligne_entiers)
    return matrice_chargee

