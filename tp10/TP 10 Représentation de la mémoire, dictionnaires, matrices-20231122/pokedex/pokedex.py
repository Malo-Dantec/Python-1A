"""Init Dev : TP10"""

# =====================================================================
# Exercice 1 : Choix de modélisation et complexité
# =====================================================================
# Modélisation n°1
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v1 dans le fichier de tests

def appartient_v1(pokemon, pokedex): 
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    for elem in pokedex:
        if pokemon in elem:           #O(N)
            return True
    return False


def toutes_les_attaques_v1(pokemon, pokedex): 
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    type = set()
    for elem in pokedex:
        if elem[0] == pokemon:           #O(N)
            type.add(elem[1])
    return type


def nombre_de_v1(attaque, pokedex): 
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    cpt = 0
    for elem in pokedex:
        if attaque == elem[1]:        #O(N)
            cpt+=1
    return cpt

def attaque_preferee_v1(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    dicofreq = dict()
    nom_attaque = None
    for elem in pokedex:
        if elem[1] in dicofreq:
            dicofreq[elem[1]] += 1         #O(N)
        else:
            dicofreq[elem[1]] = 1
    res = max(dicofreq.values())
    for (type,nb) in dicofreq.items():
        if nb == res:
            nom_attaque = type
    return nom_attaque


# =====================================================================
# Modélisation n°2
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v2 dans le fichier de tests

def appartient_v2(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    if pokemon in pokedex:                   #O(1)
            return True
    return False


def toutes_les_attaques_v2(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    if pokemon in pokedex:                 #O(1)
        return pokedex[pokemon]
    return None


def nombre_de_v2(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """
    cpt = 0
    for elem in pokedex.values():               #O(N)
        if attaque in elem:
            cpt+=1
    return cpt


def attaque_preferee_v2(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    dicofreq = {}
    nom_attaque = None
    for elem in pokedex.values():
        for type in elem:
            res = nombre_de_v2(type,pokedex)        #O(N³)
            dicofreq[type] = res
    res1 = max(dicofreq.values())
    for (nom,nb) in dicofreq.items():
        if res1 == nb:
            nom_attaque = nom
    return nom_attaque

# =====================================================================
# Modélisation n°3
# =====================================================================

# Penser à completer la fonction exemples_pokedex_v3 dans le fichier de tests


def appartient_v3(pokemon, pokedex):
    """ renvoie True si pokemon (str) est présent dans le pokedex """
    return {True for poke in pokedex.values() if pokemon in poke}    #O(N)


def toutes_les_attaques_v3(pokemon, pokedex):
    """
    param: un pokedex et le nom d'un pokemon (str) qui appartient au pokedex
    resultat: renvoie l'ensemble des types d'attaque du pokemon passé en paramètre
    """
    type_de_pokemon = set()
    for (type, poke) in pokedex.items():
        if pokemon in poke:
            type_de_pokemon.add(type)         #O(N)
    return type_de_pokemon
            


def nombre_de_v3(attaque, pokedex):
    """
    param: un pokedex et un type d'attaque (str)
    resultat: renvoie le nombre de pokemons de ce type d'attaque
    dans le pokedex
    """

    if attaque not in pokedex.keys():           #0(1)
        return 0
    return len(pokedex[attaque])


def attaque_preferee_v3(pokedex):
    """
    Renvoie le nom du type d'attaque qui est la plus fréquente dans le pokedex
    """
    dicofreq = {}
    nom_type = None
    for elem in pokedex.keys():
        dicofreq[elem] = nombre_de_v3(elem,pokedex)          #O(N)
    res = max(dicofreq.values())
    for (type,cpt) in dicofreq.items():
        if res == cpt:
            nom_type = type
    return nom_type
        

# =====================================================================
# Transformations
# =====================================================================

# Version 1 ==> Version 2

def v1_to_v2(pokedex_v1):
    """
    param: prend en paramètre un pokedex version 1
    renvoie le même pokedex mais en version 2
    """
    dico = dict()
    for elem in pokedex_v1:
        if elem[0] in dico.keys():
            dico[elem[0]].add(elem[1])               #O(N)
        else:
            types = set()
            types.add(elem[1])
            dico[elem[0]] = types
    return dico

# Version 1 ==> Version 2

def v2_to_v3(pokedex_v2):
    """
    param: prend en paramètre un pokedex version2
    renvoie le même pokedex mais en version3
    """
    dico = {}
    for (pokemon, type) in pokedex_v2.items():
        for elem in type:
            if elem in dico.keys():
                dico[elem].add(pokemon)             #O(N²)
            else:
                types = set()
                types.add(pokemon)
                dico[elem] = types
    return dico



# ========================================= #
#                Exercice 4                 #
# ========================================= #


def pokemons_par_famille(liste_pokemon):
    res = dict()
    for elem in liste_pokemon:
        for famille in elem[1]:
            if famille in res.keys():
                res[famille].add(elem[0])
            else:
                types = set()
                types.add(elem[0])
                res[famille] = types
    return res