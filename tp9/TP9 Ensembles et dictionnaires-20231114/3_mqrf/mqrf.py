
# ==========================
# La maison qui rend fou
# ==========================

def quel_guichet(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        str: le nom du guichet qui finit par donner le formulaire A-38
    """
    i = 0
    while i < len(mqrf.keys()):
        if mqrf[guichet] == None:
            return guichet
        guichet = mqrf[guichet]
        i+=1
    return None


def quel_guichet_v2(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
    """
    i = 1
    while i < len(mqrf.keys()):
        if mqrf[guichet] == None:
            return (guichet,i)
        guichet = mqrf[guichet]
        i+=1
    return None


def quel_guichet_v3(mqrf, guichet):
    """Détermine le nom du guichet qui délivre le formulaire A-38
    ainsi que le nombre de guichets visités

    Args:
        mqrf (dict): représente une maison qui rend fou
        guichet (str): le nom du guichet de départ qui est le nom d'un guichet de la mqrf

    Returns:
        tuple: le nom du guichet qui finit par donner le formulaire A-38 et le nombre de
        guichets visités pour y parvenir
        S'il n'est pas possible d'obtenir le formulaire en partant du guichet de depart,
        cette fonction renvoie None
    """
    i = 1
    while i < len(mqrf.keys()):
        if mqrf[guichet] == None:
            return (guichet,i)
        guichet = mqrf[guichet]
        i+=1
    return None

