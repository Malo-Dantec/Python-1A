import super_hero
def test_intelligence_moyenne():
    exemple2 = { 'a ' :(1 , 1 , 'a ') , 'b ' :(3 , 9 , 'b ') , 'c ' :(7 , 2 , 'c ') }
    assert super_hero.intelligence_moyenne ( exemple2 ) == 4
    exemple3 = { 'a ' :(1 , 1 , 'a ') , 'b ' :(3 , 9 , 'b ') , 'd ' :(4 , 4 , 'd ') }
    assert abs ( super_hero.intelligence_moyenne ( exemple3 ) -14/3) <= 0.01

def test_kikelplusfort():
    exemple2 = { 'a ' :(1 , 1 , 'a ') , 'b ' :(3 , 9 , 'b ') , 'c ' :(7 , 2 , 'c ') }
    assert super_hero.kikelplusfort ( exemple2 ) == 'c '
    exemple3 = { 'a ' :(1 , 1 , 'a ') , 'b ' :(3 , 9 , 'b ') , 'd ' :(4 , 4 , 'd ') }
    assert super_hero.kikelplusfort ( exemple3 ) == 'd '

def test_combienDeCretins():
    exemple2 = { 'a ' :(1 , 1 , 'a ') , 'b ' :(3 , 9 , 'b ') , 'c ' :(7 , 2 , 'c ') }
    assert super_hero.combienDeCretins ( exemple2 ) == 2
    exemple3 = { 'a ' :(1 , 1 , 'a ') , 'b ' :(3 , 9 , 'b ') , 'd ' :(4 , 4 , 'd ') }
    assert super_hero.combienDeCretins ( exemple3 ) == 2