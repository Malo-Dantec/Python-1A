""" TP7 une application complète
    ATTENTION VOUS DEVEZ METTRE DES DOCSTRING A TOUTES VOS FONCTIONS
"""
def afficher_menu(titre, liste_options):
    ligne_tiret = "-"*len(titre)
    ligne_vide = " "*len(titre)
    print()
    print()
    print("+----"+ligne_tiret+"----+")
    print("|    "+ligne_vide+"    |")
    print("|    "+titre+"    |")
    print("|    "+ligne_vide+"    |")
    print("+----"+ligne_tiret+"----+")
    print()
    for i in range(len(liste_options)):
        print(i+1, " --> ", liste_options[i])
    print()
# afficher_menu("Imad Assou bien garni", 
#                     ["Charger un fichier",
#                      "Rechercher la population d'une commune",
#                      "Afficher la population d'un département", 
#                      "Quitter"])




def demander_nombre(message, borne_max):
    try:
        nombre = input(message)
        if nombre.isdecimal():
            nombre = int(nombre)
            if 1 <= nombre <= borne_max:
                return int(nombre)
            else:
                print("Entrez un nombre entre 1 et "+str(borne_max)+".")
    except:
        return None
# print(demander_nombre("Entrez votre choix [1-4] : ",4))




def menu(titre, liste_options):
    afficher_menu(titre, liste_options)
    choix_utilisateur = demander_nombre("Entrez votre choix [1-"+str(len(liste_options))+"] : ", len(liste_options))
    if choix_utilisateur is not None:
        return choix_utilisateur
    else:
        return None
# print(menu("MENU DE MON APPLICATION", ["Charger un fichier",
#                      "Rechercher la population d'une commune",
#                      "Afficher la population d'un département", 
#                      "Quitter"]))





def programme_principal():
    liste_options = ["Charger un fichier",
                     "Rechercher la population d'une commune",
                     "Rechercher des communes commençant par une chaine de caractère",
                     "Afficher la population d'un département", 
                     "Quitter"]
    liste_communes = []
    while True:
        rep = menu("MENU DE MON APPLICATION", liste_options)
        if rep is None:
            print("Cette option n'existe pas")
        elif rep == 1:
            print("Vous avez choisi", liste_options[rep - 1])
            print("Choisissez un nom de fichier parmi les suivants : extrait1.csv ; extrait2.csv ; population2007.csv ; population2017.csv")
            reponse = input()
            reponse = str(reponse)
            try:
                result = charger_fichier_population(reponse)
                print(result)
            except:
                print("Ce fichier n'existe pas.")
        elif rep == 2:
            print("Vous avez choisi", liste_options[rep - 1])
            print("Choisissez le nom d'un fichier.")
            fic = input()
            fic = str(fic)
            print("Choisissez le nom d'une ville.")
            ville = input()
            ville = str(ville)
            try:
                result = population_d_une_commune(charger_fichier_population(fic),ville)
                print('\033[93m'"La population de la cummune",ville,"est de",result,""'\033[0m')
            except:
                print('\033[93m'"Le fichier n'existe pas ou la ville n'existe pas dans la liste souhaitée."'\033[0m')
        elif rep == 3:
            print("Vous avez choisi", liste_options[rep - 1])
            print("Choisissez le nom d'un fichier.")
            fic = input()
            fic = str(fic)
            print("Choisir le commencement du nom d'une ville.")
            com = input()
            com = str(com)
            try:
                result = liste_des_communes_commencant_par(charger_fichier_population(fic),com)
                print('\033[93m'"Les communes commençant par la chaine de caractère",com,"sont :",result,'\033[0m')
            except:
                print('\033[93m'"Le fichier n'existe pas ou la ville n'existe pas dans la liste souhaitée."'\033[0m')
        elif rep ==4:
            print("Vous avez choisi", liste_options[rep - 1])
        else:
            break
        input("Appuyer sur Entrée pour continuer")
    print("Merci au revoir!")




def charger_fichier_population(nom_fic):
    res = []
    fic = open(nom_fic, "r")
    fic.readline()
    for ligne in fic:
        val = ligne.split(";")
        res.append((str(val[0]),str(val[1]),int(val[4])))
    fic.close()
    return res

def population_d_une_commune(liste_pop, nom_commune):
    for i in range(len(liste_pop)):
        if nom_commune == liste_pop[i][1]:
            result = liste_pop[i][2]
    return result
# print(population_d_une_commune(charger_fichier_population('extrait1.csv'),'Olivet'))

def liste_des_communes_commencant_par(liste_pop, debut_nom):
    res = []
    j = 0
    taille=len(debut_nom)
    for i in range(len(liste_pop)):
        j=0
        while j != taille:
            if debut_nom[j]==liste_pop[i][1][j]:
                j+=1
                if j==taille:
                    res.append(liste_pop[i][1])
            else:
                break
    return res
# print(liste_des_communes_commencant_par(charger_fichier_population('extrait1.csv'),'Orl'))

def commune_plus_peuplee_departement(liste_pop, num_dpt):
    res = 0
    ville = ""
    for villes in liste_pop:
        if villes[0].startswith(str(num_dpt)) and villes[2]>res:
            res = villes[2]
            ville = villes[1]
    return ville
# print(commune_plus_peuplee_departement(charger_fichier_population('extrait2.csv'),'18'))
def nombre_de_communes_tranche_pop(liste_pop, pop_min, pop_max):
    res = []
    for i in range(len(liste_pop)):
        if liste_pop[i][2] > pop_min and liste_pop[i][2] < pop_max:
            res.append(liste_pop[i][1])
    return res
print(nombre_de_communes_tranche_pop(charger_fichier_population('extrait2.csv'),1,10000))

def place_top(commune, liste_pop):
    

def ajouter_trier(commune, liste_pop, taille_max):
    ...


def top_n_population(liste_pop, nbre):
    ...

def population_par_departement(liste_pop):
    ...

def sauve_population_dpt(nom_fic, liste_pop_dep):
    ...

# appel au programme principal
# programme_principal()
