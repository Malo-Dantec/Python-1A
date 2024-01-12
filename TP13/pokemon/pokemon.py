"""
Un pokedex est modélisé par une liste contenant des informations sur des pokemons.
Ces informations sont données sous la forme d'un tuple (nom, familles, attaque, défense, poids).
"""

def mon_pokedex():
    """ renvoie mon pokedex avec la structure de données
        donnée dans la documentaion du module """
    return [('Bulbizarre', {'Plante', 'Poison'}, 4, 3, 7),
            ('Jungko', {'Plante'}, 7, 1, 52),
            ('Herbizarre', {'Plante', 'Poison'}, 5, 5, 13),            
            ('Abo', {'Poison'}, 4, 2, 6)]

def get_attaque(pokemon):
    return pokemon[2]


def plus_forte_attaque(pokedex):
    def atq(pokemon):
        return pokemon[2]
    return sorted(pokedex, key=atq)[-1]


def tri_selon_defense(pokedex):
    def defense(pokemon):
        return pokemon[3]
    tri = sorted(pokedex, key=defense)
    poke_tri = []
    for poke in tri:
        poke_tri.append(poke[0])
    return poke_tri


def plus_petite_force(pokedex):
    def force(pokemon):
        return pokemon[2] + pokemon[3]
    return sorted(pokedex, key=force)[0][0]


def tri_selon_diversite(pokedex):
    def diversite(pokemon):
        return len(pokemon[1])
    m = sorted(pokedex, key=get_attaque)
    return sorted(m, key=diversite)