import os

os.system('cls')



conj = {
    'casa',
    "peteca",
    122,
    True,
    1999.90,
    (10, 'mola')
}

alunas = [
    ('Maria', '2000-10-14', 'A'),
    ('Joana', '1997-08-10', 'A'),
    # ...
]

print(f'{alunas[1][0]} nasceu em {alunas[1][1]}')
print(alunas[1][0] + ' nasceu em ' + alunas[1][1])
print(alunas[1][0], 'nasceu em', alunas[1][1])

# Conjuntos

import os
os.system('cls')

conj = {
    'casa',
    "peteca",
    122,
    True,
    1999.90,
    (10, 'mola'),
    122,122,122,122,122,122,122,122,122,
} 

print(conj)
# print(conj[1]) ERRO!
print(len(conj))