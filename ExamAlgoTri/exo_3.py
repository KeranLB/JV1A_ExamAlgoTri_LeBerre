### Import ###
from random import randint
######

### tableau ###
myTable = []

for _ in range(randint(1,10)):
    myTable += [randint(1,10)]

print(myTable)
######

### definitoins ###

def permuter(tab, indice_a, indice_b):
    tmp = tab[indice_a]
    tab[indice_a] = tab[indice_b]
    tab[indice_b] = tmp
    return tab

assert permuter([3,2,1],0,1) == [2,3,1]


def iteration(myTable):
    for i in range(len(myTable)-1):
        if myTable[i] > myTable[i+1]:
            myTable = permuter(myTable, i, i+1)
    return myTable

assert iteration([3,1,2]) == [1,2,3]
######

### MAIN ###

for _ in range(len(myTable)):
    iteration(myTable)

print(myTable)

######