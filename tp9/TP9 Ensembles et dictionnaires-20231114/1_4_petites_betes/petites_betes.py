"""Init Dev : TP9"""


# ==========================
# Petites bêtes
# ==========================

mon_pokedex = [("Bulbizarre","Plante"),("Aeromite","Poison"),("Abo","Poison")] 

def toutes_les_familles(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    famille = set()  #O(1)
    for (_,type) in pokedex: #O(n)
        famille.add(type)  #O(1)             fonction O(n)
    return famille  #O(1)
def test_toutes_les_familles():
    assert toutes_les_familles(mon_pokedex) == {"Plante","Poison"}



def nombre_pokemons(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    nb = 0
    for (_,type) in pokedex:
        if famille == type:
            nb+=1
    return nb
def test_nombre_pokemons():
    assert nombre_pokemons ( mon_pokedex , "Poison" ) == 2
    assert nombre_pokemons ( mon_pokedex , "Insecte") == 0



def frequences_famille(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str)
        et la valeur associée est le nombre de représentants de la famille (int)
    """
    # res = dict()
    # lesFamilles = toutes_les_familles(pokedex)
    # for famille in lesFamilles:
    #     res[famille] = nombre_pokemons(pokedex, famille)
    # return res
    res = dict()
    for (_,famille) in pokedex:
        if famille in res.keys():
            res[famille] += 1
        else:
            res[famille] = 1
    return res
def test_frequences_famille():
    assert frequences_famille ( mon_pokedex ) == {"Plante": 1 , "Poison" : 2}



def dico_par_famille(pokedex):
    """Construit un dictionnaire dont les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de cette
    famille dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    res = dict()
    for famille in toutes_les_familles(pokedex):
        res1 = set()
        for i in range(len(pokedex)):
            if famille == pokedex[i][1]:
                res1.add(pokedex[i][0])
        res[famille] = res1
    return res
def test_dico_par_famille():
    assert dico_par_famille(mon_pokedex) == {'Poison': {'Abo', 'Aeromite'}, 'Plante': {'Bulbizarre'}}

def famille_la_plus_representee(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (list): liste de pokemon, chaque pokemon est modélisé par
        un couple de str (nom, famille)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    Famille = None
    max = 0
    res = frequences_famille(pokedex)
    for (nom, nombre) in res.items():
        if max < nombre:
            max = nombre
            Famille = nom
    return Famille
def test_famille_la_plus_representee():
    assert famille_la_plus_representee(mon_pokedex) == 'Poison'
        


# ==========================
# Petites bêtes (la suite)
# ==========================

mon_pokedex1 = {"Bulbizarre" :{ "Plante" ,"Poison"} , "Aeromite" :{"Poison" ,"Insecte" }, "Abo" :{ "Poison" }}
def toutes_les_familles_v2(pokedex):
    """détermine l'ensemble des familles représentées dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        set: l'ensemble des familles représentées dans le pokedex
    """
    res = set()
    for famille in pokedex.values():
        for elem in famille:
            res.add(elem)
    return res
def test_toutes_les_familles_v2():
    assert toutes_les_familles_v2(mon_pokedex1) == { "Plante" , "Poison" , "Insecte" }


def nombre_pokemons_v2(pokedex, famille):
    """calcule le nombre de pokemons d'une certaine famille dans un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)
        famille (str): le nom de la famille concernée

    Returns:
        int: le nombre de pokemons d'une certaine famille dans un pokedex
    """
    nb = 0
    for type in pokedex.values():
        for elem in type:
            if elem == famille:
                nb+=1
    return nb
def test_nombre_pokemons_v2():
    assert nombre_pokemons_v2(mon_pokedex1, "Poison" ) == 3


def frequences_famille_v2(pokedex):
    """Construit le dictionnaire de fréqeunces des familles d'un pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur
        associée est le nombre de représentants de la famille (int)
    """
    res = dict()
    for type in pokedex.values():
        for famille in type:
            if famille in res:
                res[famille]+=1
            else:
                res[famille]=1
    return res
def test_frequences_famille_v2():
    assert frequences_famille_v2(mon_pokedex1) == {"Plante": 1, "Poison": 3, "Insecte": 1}

def dico_par_famille_v2(pokedex):
    """Construit un dictionnaire dont les les clés sont le nom de familles (str)
    et la valeur associée est l'ensemble (set) des noms des pokemons de
    cette famille dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        dict: un dictionnaire dont les clés sont le nom de familles (str) et la valeur associée est
        l'ensemble (set) des noms des pokemons de cette famille dans le pokedex
    """
    dico_famille=dict()
    for (nom,famillesss) in pokedex.items():
        for famille in famillesss:
            if famille not in dico_famille.keys():
                dico_famille[famille]={nom}
            else:
                dico_famille[famille].add(nom)
    return dico_famille
def test_dico_par_famille_v2():
    assert dico_par_famille_v2 (mon_pokedex1) == {"Plante": {"Bulbizarre"},"Poison" : {"Bulbizarre" , "Aeromite" , "Abo" }, "Insecte": {"Aeromite" }}
def famille_la_plus_representee_v2(pokedex):
    """détermine le nom de la famille la plus représentée dans le pokedex

    Args:
        pokedex (dict): un dictionnaire dont les clés sont les noms de pokemons et la
        valeur associée l'ensemble (set) de ses familles (str)

    Returns:
        str: le nom de la famille la plus représentée dans le pokedex
    """
    famille_freq=frequences_famille_v2(pokedex)
    grosse_famille=None
    grosse_freq_famille=0
    for (famille,cpt) in famille_freq.items():
        if cpt> grosse_freq_famille:
            grosse_famille=famille
            grosse_freq_famille=cpt
    return grosse_famille
