def syracuse(n):
    liste = []
    liste.append(n)
    while n != 1:
        if n%2 == 0:
            n //= 2
        else:
            n = 3*n +1
        liste.append(n)
    return liste

# print(syracuse(2))
# print(syracuse(3))
# print(syracuse(5))

# print(len(syracuse(27)))

def temps_de_vol(n):
    return len(syracuse(n))-1

# print(temps_de_vol(10))

def champion(n):
    plus_long = 0
    for nombre in range(1, n):
        if temps_de_vol(nombre) > plus_long:
            plus_long = nombre
    return plus_long

# print(champion(27))

# def temps_de_vol_avec_precalcul(n, temps_connus):

