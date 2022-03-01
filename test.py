def suite_syracuse(n):
    """
    Retourne la suite de Syracuse pour l'entier n.
    >>> suite_syracuse(15)
    [15, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """

    seq = [n]                     # La suite de Syracuse sera complétée...
    while seq[-1] != 1:           # ...jusqu'à tomber sur 1
        if seq[-1] % 2 == 0:      # u_n est pair
            seq.append(seq[-1] // 2)  # Division euclidienne par 2
        else:                     # u_n est impair
            seq.append(seq[-1] * 3 + 1)

    return seq
n = int(input("entrer nombre sup à 1 : "))
print(suite_syracuse(n))