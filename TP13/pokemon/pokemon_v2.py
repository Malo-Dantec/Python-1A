"""
Un pokedex est modélisé par un dictionnaire dont les clefs sont les noms des pokemons 
et les valeurs associée des informations sur des pokemons.
Ces informations sont données sous la forme d'un tuple (familles, attaque, défense, poids).
"""

def mon_pokedex():
    """ renvoie mon pokedex avec la structure de données
        donnée dans la documentaion du module """
    return {'Bulbizarre': ({'Plante', 'Poison'}, 4, 3, 7),
            'Jungko': ({'Plante'}, 7, 1, 52),
            'Herbizarre': ({'Plante', 'Poison'}, 5, 5, 13),            
            'Abo': ({'Poison'}, 4, 2, 6)}

def plus_forte_attaque(pokedex):
    ...


def tri_selon_defense(pokedex):
    ...


def plus_petite_force(pokedex):
    ...


def tri_selon_diversite(pokedex):
    ...

