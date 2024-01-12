import pokemon_v3 as pokemon

def test_plus_forte_attaque():
    exemple = pokemon.mon_pokedex()
    assert pokemon.plus_forte_attaque(exemple) == ('Jungko', {'Plante'}, 7, 1, 52)

def test_tri_selon_defense():
    exemple = pokemon.mon_pokedex()
    assert pokemon.tri_selon_defense(exemple) == ['Jungko', 'Abo', 'Bulbizarre', 'Herbizarre']
    
def test_plus_petite_force():
    exemple = pokemon.mon_pokedex()
    assert pokemon.plus_petite_force(exemple) == 'Abo'


def test_tri_selon_diversite():
    exemple = pokemon.mon_pokedex()
    pokemon.tri_selon_diversite(exemple)
    assert pokemon.tri_selon_diversite(exemple) == \
        [('Abo', {'Poison'}, 4, 2, 6),
         ('Jungko', {'Plante'}, 7, 1, 52),
         ('Bulbizarre', {'Plante', 'Poison'}, 4, 3, 7), 
         ('Herbizarre', {'Plante', 'Poison'}, 5, 5, 13),]
