import math

def aire_cercle_diametre(diametre):
    rayon = diametre / 2
    return math.pi * rayon ** 2

# exemple test
print(aire_cercle_diametre(10))