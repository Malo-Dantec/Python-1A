"""
Un pokedex est modélisé par un dictionnaire dont les clefs sont les noms des pokemons 
et les valeurs associée des informations sur des pokemons.
Ces informations sont données sous la forme d'un dictionnaire.
"""

def mon_pokedex():
    """ renvoie mon pokedex avec la structure de données
        donnée dans la documentaion du module """
    return {'Bulbizarre': {'familles':{'Plante', 'Poison'}, 
                           'attaque':4, 
                           'defense':3, 
                           'poids':7},
            'Herbizarre': {'familles':{'Plante', 'Poison'}, 
                           'attaque':5, 
                           'defense':5, 
                           'poids':13},
            'Jungko': {'familles':{'Plante'}, 
                       'attaque':7, 
                       'defense':1, 
                       'poids':52},
            'Abo': {'familles':{'Poison'}, 
                    'attaque':4, 
                    'defense':2, 
                    'poids':6}}


def plus_forte_attaque(pokedex):
    ...


def tri_selon_defense(pokedex):
    ...


def plus_petite_force(pokedex):
    ...


def tri_selon_diversite(pokedex):
    ...
