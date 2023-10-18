### Import ###
from random import randint
######

### tableau ###
myTable = []

for _ in range(randint(1,10)):
    myTable += [randint(1,10)]

print(myTable)
######

### definition ###

def permuter(tab, indice_a, indice_b):
    tmp = tab[indice_a]
    tab[indice_a] = tab[indice_b]
    tab[indice_b] = tmp
    return tab

assert permuter([3,2,1],0,1) == [2,3,1]
######