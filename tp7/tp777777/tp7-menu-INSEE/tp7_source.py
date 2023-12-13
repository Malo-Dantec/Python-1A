""" TP7 une application complète
    ATTENTION VOUS DEVEZ METTRE DES DOCSTRING A TOUTES VOS FONCTIONS
"""
def afficher_menu(titre, options):
    print("+---------------------------+")
    # Affiche le titre centré dans une boîte de largeur 25
    print(f"| {titre.center(25)} |")
    print("+---------------------------+")
    # Itère sur la liste d'options en commençant par 1 pour le numéro
    for i, option in enumerate(options, start=1):
        # Affiche chaque option numérotée et son contenu
        print(f"{i} -> {option}")
    # Affiche une ligne vide
    print()
options_menu = ["Charger un fichier", "Rechercher la population d'une commune", "Afficher la population d'un département", "Quitter"]
titre_menu = "MENU DE MON APPLICATION"
afficher_menu(titre_menu, options_menu)




# Définition de la fonction demander_choix avec deux paramètres : message et borne_max
def demander_choix(message, borne_max):
    try:
        # Demande à l'utilisateur d'entrer un message et stocke la valeur dans la variable choix
        choix = input(message)
        # Vérifie si l'entrée de l'utilisateur est un nombre décimal
        if choix.isdecimal():
            # Convertit le choix en entier
            choix = int(choix)
            # Vérifie si le choix est dans la plage autorisée (entre 1 et borne_max inclus)
            if 1 <= choix <= borne_max:
                # Retourne le choix de l'utilisateur s'il est valide
                return choix
            else:
                # Affiche un message d'erreur si le choix n'est pas dans la plage autorisée
                print(f"Veuillez entrer un nombre entre 1 et {borne_max}.")
        else:
            # Affiche un message d'erreur si l'entrée de l'utilisateur n'est pas un nombre décimal
            print("Veuillez entrer un nombre entier.")
    except Exception as e:
        # Affiche un message d'erreur si une exception se produit pendant l'exécution du code
        print(f"Erreur : {e}")
    # Retourne None si l'entrée de l'utilisateur est incorrecte ou si une exception se produit
    return None

# Exemple d'utilisation de la fonction
# Définit la borne maximale pour le choix de l'utilisateur
borne_max = 4
# Crée le message d'invite en incluant la borne maximale
message_invite = "Entrez votre choix [1-{}]: ".format(borne_max)
# Appelle la fonction demander_choix avec le message d'invite et la borne maximale
choix_utilisateur = demander_choix(message_invite, borne_max)

# Vérifie si le choix de l'utilisateur est valide
if choix_utilisateur is not None:
    # Affiche le choix de l'utilisateur s'il est valide
    print("Vous avez choisi l'option", choix_utilisateur)
else:
    # Affiche un message si le choix de l'utilisateur n'est pas valide
    print("Choix invalide.")





def menu(titre, options):
    # Affiche le menu en utilisant la fonction afficher_menu précédemment définie.
    afficher_menu(titre, options)
    # Demande à l'utilisateur son choix.
    choix_utilisateur = demander_choix("Entrez votre choix [1-{}]: ".format(len(options)), len(options))
    # Vérifie si le choix de l'utilisateur est valide.
    if choix_utilisateur is not None:
        return choix_utilisateur
    else:
        print("Choix invalide.")
        return None




def programme_principal():
    liste_options = ["Charger un fichier",
                     "Rechercher la population d'une commune",
                     "Afficher la population d'un département", 
                     "Quitter"]
    liste_communes = []
    while True:
        rep = menu("MENU DE MON APPLICATION", liste_options)
        if rep is None:
            print("Cette option n'existe pas")
        elif rep == 1:
            print("Vous avez choisi", liste_options[rep - 1])
        elif rep == 2: 
            print("Vous avez choisi", liste_options[rep - 1])
        elif rep == 3:
            print("Vous avez choisi", liste_options[rep - 1])
        else:
            break
        input("Appuyer sur Entrée pour continuer")
    print("Merci au revoir!")




def charger_fichier_population(nom_fic):
    ...

def population_d_une_commune(liste_pop, nom_commune):
    ...

def liste_des_communes_commencant_par(liste_pop, debut_nom):
    ...

def commune_plus_peuplee_departement(liste_pop, num_dpt):
    ...

def nombre_de_communes_tranche_pop(liste_pop, pop_min, pop_max):
    ...

def place_top(commune, liste_pop):
    ...

def ajouter_trier(commune, liste_pop, taille_max):
    ...


def top_n_population(liste_pop, nbre):
    ...

def population_par_departement(liste_pop):
    ...

def sauve_population_dpt(nom_fic, liste_pop_dep):
    ...

# appel au programme principal
programme_principal()
