n = int(input("entrer une valeur : "))
p = int(input("entrer une valeur : "))
def multiplication(n, p):
    """ Renvoie le produit de n par p """
    produit = 0
    while n != 0:
        if n % 2 == 1:  # multiplicateur impair
            produit += p
        n //= 2 # division euclidienne par 2 du multiplicateur
        p *= 2 # multiplication par 2 du multiplicande
    return produit

print(multiplication(n,p))