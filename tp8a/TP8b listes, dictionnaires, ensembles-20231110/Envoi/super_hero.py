def intelligence_moyenne(dictionnaire):
    res = 0
    res1 = 0
    for hero in dictionnaire.values():
        res += hero[1]
        res1+=1
    res = res/res1
    if res1 == 0:
        return None
    return res

def kikelplusfort(dictionnaire):
    nom = None
    plus_fort = 0
    for (hero,stats) in dictionnaire.items():
        if stats[0] > plus_fort:
            plus_fort = stats[0]
            nom = hero
    return nom

def combienDeCretins(dictionnaire):
    con = 0
    for (hero,stats) in dictionnaire.items():
        if stats[1] < intelligence_moyenne(dictionnaire):
            con += 1
    return con