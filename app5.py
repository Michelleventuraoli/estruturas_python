age = int(input('Digite a idade: '))
has_invitation = bool(input('Tem convite [sim/não]? '))
is_vip = True

# Depuração de variáveis
print(type(age), age)
print(type(has_invitation), has_invitation)
print(type(is_vip), is_vip)


'''
if is_vip:
    print('Que bom ver você novamente')    

elif age >= 18 and has_invitation:
    print("Entrada permitida") 

else: 
    print("Entrada não permitida") 

'''

print("Acabou")


import os

# Limpa a tela do terminal CMD
os.system("cls")

age = int(input('Digite a idade: '))
invited = input('Tem convite [sim/não]? ')
is_vip = True

# Define o valor da variável
has_invitation = False

# Testa a entrada do usuário
if invited == 'sim':
    # Neste caso, altera o valor da variável
    has_invitation = True

# Depuração de variáveis
print("age", type(age), age)
print("has_invitation", type(has_invitation), has_invitation)
print("is_vip", type(is_vip), is_vip)


'''
if is_vip:
    print('Que bom ver você novamente')    

elif age >= 18 and has_invitation:
    print("Entrada permitida") 

else: 
    print("Entrada não permitida") 

'''

print("Acabou")


import os

os.system("cls")

fruits = ['maçã', 'banana', 'pera', 'uva', 'morango']

print(fruits)

for fruit in fruits:
    print(f' • {fruit};')

print('\nAcabou')