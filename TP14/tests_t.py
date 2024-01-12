"""Fonctions de tests pour le TP 14"""

import t as tp14

# EXERCICE 1

def test_recette_la_plus_facile():
    lundi = {'Carottes rapées': (15, 1), 'Nouilles au beurre':(20, 2), 'Mousse au chocolat':(30, 7)}
    mardi = {'Soupe': (40, 3), 'Steak':(20, 4), 'Fromage':(1, 0)  }
    mercredi = {'Pizza': (20, 1), 'Omelette':(15, 3), 'Pomme au four':(10, 2)}
    jeudi = dict() # jour de diète
    assert tp14.recette_la_plus_facile(lundi) == 'Carottes rapées'
    assert tp14.recette_la_plus_facile(mardi) == 'Fromage'
    assert tp14.recette_la_plus_facile(jeudi) is None
    assert tp14.recette_la_plus_facile(mercredi) == ...


def test_temps_total_de_preparation():
    lundi = {'Carottes rapées': (15, 1), 'Nouilles au beurre':(20, 2), 'Mousse au chocolat':(30, 7)}
    mardi = {'Soupe': (40, 3), 'Steak':(20, 4), 'Fromage':(1, 0)  }
    mercredi = {'Pizza': (20, 1), 'Omelette':(15, 3), 'Pomme au four':(10, 2)}
    jeudi = dict() # jour de diète
    assert tp14.temps_total_de_preparation(lundi) == 65
    assert tp14.temps_total_de_preparation(mardi) == 61
    assert tp14.temps_total_de_preparation(jeudi) == 0
    assert tp14.temps_total_de_preparation(mercredi) == ...


def test_menu_de_chef():
    lundi = {'Carottes rapées': (15, 1), 'Nouilles au beurre':(20, 2), 'Mousse au chocolat':(30, 7)}
    mardi = {'Soupe': (40, 3), 'Steak':(20, 4), 'Fromage':(1, 0)  }
    mercredi = {'Pizza': (20, 1), 'Omelette':(15, 3), 'Pomme au four':(10, 2)}
    jeudi = dict() # jour de diète
    assert tp14.menu_de_chef(lundi)
    assert not tp14.menu_de_chef(mardi)
    assert not tp14.menu_de_chef(jeudi)
    assert tp14.menu_de_chef(mercredi) == ...


def test_recette_la_plus_longue():
    lundi = {'Carottes rapées': (15, 1), 'Nouilles au beurre':(20, 2), 'Mousse au chocolat':(30, 7)}
    mardi = {'Soupe': (40, 3), 'Steak':(20, 4), 'Fromage':(1, 0)  }
    mercredi = {'Pizza': (20, 1), 'Omelette':(15, 3), 'Pomme au four':(10, 2)}
    jeudi = dict() # jour de diète
    assert tp14.recette_la_plus_longue(lundi) == 'Mousse au chocolat'
    assert tp14.recette_la_plus_longue(mardi) == 'Soupe'
    assert tp14.recette_la_plus_longue(jeudi) is None
    assert tp14.recette_la_plus_longue(mercredi) == ...

def test_recettes_triee_par_temps():
    lundi = {'Carottes rapées': (15, 1), 'Nouilles au beurre':(20, 2), 'Mousse au chocolat':(30, 7)}
    mardi = {'Soupe': (40, 3), 'Steak':(20, 4), 'Fromage':(1, 0)  }
    mercredi = {'Pizza': (20, 1), 'Omelette':(15, 3), 'Pomme au four':(10, 2)}
    jeudi = dict() # jour de diète
    assert tp14.recettes_triee_par_temps(lundi) == ['Carottes rapées', 'Nouilles au beurre', 'Mousse au chocolat']
    assert tp14.recettes_triee_par_temps(mardi) == ['Fromage', 'Steak', 'Soupe']
    assert tp14.recettes_triee_par_temps(jeudi) == []
    assert tp14.recettes_triee_par_temps(mercredi) == ...

def test_recettes_triee_par_difficulte():
    lundi = {'Carottes rapées': (15, 1), 'Nouilles au beurre':(20, 2), 'Mousse au chocolat':(30, 7)}
    mardi = {'Soupe': (40, 3), 'Steak':(20, 4), 'Fromage':(1, 0)  }
    mercredi = {'Pizza': (20, 1), 'Omelette':(15, 3), 'Pomme au four':(10, 2)}
    jeudi = dict() # jour de diète
    assert tp14.recettes_triee_par_difficulte(lundi) == ['Carottes rapées', 'Nouilles au beurre', 'Mousse au chocolat']
    assert tp14.recettes_triee_par_difficulte(mardi) == ['Fromage', 'Soupe', 'Steak']
    assert tp14.recettes_triee_par_difficulte(jeudi) == []
    assert tp14.recettes_triee_par_difficulte(mercredi) == ...

# EXERCICE 2

def test_reglement():
    mon_porte_monnaie = [2, 20, 20, 50, 100, 20, 5, 5, 2, 1]
    assert tp14.reglement(47, mon_porte_monnaie) == [20, 20, 5, 2]
    assert tp14.reglement(10000, mon_porte_monnaie) == None
    assert tp14.reglement(60, [20, 50, 20, 20]) == ...
    assert tp14.reglement(55, [20, 50, 20, 20]) == ...

# EXERCICE 3

def test_duellistes():
    novembre_2020 = {'Jasmine': 1400, 'Will': 1610, 'Zoé': 1100, 
                     'Sasha': 2005, 'Théo': 700, 'Morgan': 1700, 
                     'Maxime': 1650, 'Florent': 1800, 'Olive': 1500}
    decembre_2020 = {'Jasmine': 1510, 'Zoé': 980, 'Morgan': 1650, 
                     'Sasha': 1880, 'Olive': 1670, 'Florent': 1810, 
                     'Will': 1460, 'Théo': 850, 'Maxime': 1400}
    assert tp14.duellistes(novembre_2020) == {'Will', 'Maxime'}
    assert tp14.duellistes(decembre_2020) == {'Morgan', 'Olive'}
