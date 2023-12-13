import motdepasse

# --------------------------------------
# FONCTIONS
# --------------------------------------

def test_longueur_ok():
    assert motdepasse.longueur_ok("choubouilli") # longueur ok
    assert not motdepasse.longueur_ok("chou") # longueur pas ok
    assert not motdepasse.longueur_ok("") # chaine vide


def test_chiffre_ok():
    assert motdepasse.chiffre_ok("c3hou9boui2lli")  # chiffre au milieu
    assert motdepasse.chiffre_ok("7c1h2oubouilli")  # chiffre au début
    assert motdepasse.chiffre_ok("chouboui7ll9i5")  # chiffre à la fin
    assert motdepasse.chiffre_ok("1chou3boui8lli")  # deux chiffres    
    assert not motdepasse.chiffre_ok("chou")       # pas de chiffres
    assert not motdepasse.chiffre_ok("un deux trois") # pas de chiffres


def test_sans_espace():
    assert motdepasse.sans_espace("choubouilli") # sans espace ok
    assert not motdepasse.sans_espace("chou bouilli") # espace au milieu
    assert not motdepasse.sans_espace(" choubouilli") # espace au début
    assert not motdepasse.sans_espace("choubouilli ") # espace à la fin
    assert motdepasse.sans_espace("") # chaine vide


def test_double_chiffre():
    assert motdepasse.double_chiffre("3dzdizjdi3ihzifzifj3")
    assert not motdepasse.double_chiffre("333fezfezffz")
    assert not motdepasse.double_chiffre("2fefefefe15")


def test_petit_chiffe():
    assert not motdepasse.petit_chiffre("1ihoihiooj1oijojo4")
    assert motdepasse.petit_chiffre("1zfzfz2gegzeg2")
    assert not motdepasse.petit_chiffre("222diezjfzejiofze")