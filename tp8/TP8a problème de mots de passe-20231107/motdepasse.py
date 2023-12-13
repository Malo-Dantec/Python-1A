def longueur_ok(mot_de_passe):
    return len(mot_de_passe) >= 8
def chiffre_ok(mot_de_passe):
    nb_chiffre = 0
    for lettre in mot_de_passe:
        if lettre.isdigit():
            nb_chiffre += 1
        if nb_chiffre >= 3:
            return True
    return False
def double_chiffre(mot_de_passe):
    for i in range(1,len(mot_de_passe)):
        if mot_de_passe[i].isdigit() and mot_de_passe[i-1].isdigit():
            return False
    return True
def petit_chiffre(mot_de_passe):
    nb_petit_chiffre = 0
    petit_chiffre = None
    for lettre in mot_de_passe:
        if lettre.isdigit():
            if petit_chiffre == None:
                petit_chiffre = lettre
            elif lettre < petit_chiffre:
                petit_chiffre = lettre
    for i in range(len(mot_de_passe)):
        if mot_de_passe[i] == petit_chiffre:
            nb_petit_chiffre += 1
        if nb_petit_chiffre > 1:
            return False
    return True
def sans_espace(mot_de_passe):
    for lettre in mot_de_passe:
        if lettre == " ":
            return False
    return True

def dialogue_mot_de_passe():
    login = input("Entrez votre nom : ")
    mot_de_passe_correct = False
    while not mot_de_passe_correct :
        mot_de_passe = input("Entrez votre mot de passe : ")
        if not longueur_ok(mot_de_passe):
            print("Votre mot de passe doit comporter au moins 8 caractères")
        elif not chiffre_ok(mot_de_passe):
            print("Votre mot de passe doit comporter au moins trois chiffres")
        elif not double_chiffre(mot_de_passe):
            print("Votre mot de passe ne doit pas contenir 2 chiffres consécutifs")
        elif not petit_chiffre(mot_de_passe):
            print("Le chiffre le plus petit doit apparaître une seule fois")
        elif not sans_espace(mot_de_passe):
            print("Votre mot de passe ne doit pas comporter d'espace")	   
        else:
            mot_de_passe_correct = True
    print("Votre mot de passe est correct")
    return mot_de_passe
dialogue_mot_de_passe()

def ecrire(nom,login,mot_de_passe):
    fic = open(nom, 'a')
    fic.write(login+ " : ")
    fic.write(mot_de_passe+ '\n')
    fic.close()

def crampté(nom):
    """retourne le dictionnaire composé des login : mdp contenus dans le fichier"""
    logins = dict()
    fic = open(nom, 'r')
    login = fic.readline()[:-1]
    while login != "":
        mdp = fic.readline()[:-1]
        logins[login] = mdp
        login = fic.readline()[:-1]
    fic.close()
    return logins

dico = crampté("mdpUltraSecret.txt")
# print(dico)

def ecrire_logins(nom, dico):
    fic = open(nom, 'w')
    for (login,mot_de_passe) in dico.items():
        fic.write(login+'\n')
        fic.write(mot_de_passe+'\n')
    fic.close()
