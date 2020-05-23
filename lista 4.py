##LISTA DE EXERCÍCIO 4:

##EXERCÍCIO 1:

from random import randint
vet = []
for i in range(0, 10):
    n1 = randint (1, 100)
    vet.append(n1)
maior = vet[0]
menor = vet[0]
for k in range(0, 9):
    if maior < vet[k]:
        maior = vet[k]
    if menor > vet[k]:
        menor = vet[k]
print(f"VETOR: {vet}")  

print(f"O menor número da lista é: {menor}, e o maior número da lista é: {maior}")
print("-------------------------------------------------------")

##EXERCÍCIO 2:

from random import randint
vet = []
par = []
impar = []
for i in range (0, 20):
    n = randint (1, 100)
    vet.append(n)
##Aqui encontramos os números pares:
    for x in range(0, 20):
        num_par = vet[i]
    if num_par%2 == 0:
        par.append(num_par)
##Aqui encontramos os números ímpares:
    for y in range(0, 20):
        num_impar = vet[i]
    if num_impar%2 != 0:
        impar.append(num_impar)
print(f"VETOR:{vet}")
print(f"PAR:{par}")
print(f"ÍMPAR: {impar}")
print("-------------------------------------------------------")

##EXERCÍCO 3:
from random import randint
vetor1 = []
vetor2 = []
vetor3 = []
for i in range(0, 10):
    n = randint(1, 100)
    vetor1.append(n)
    n1 = randint(1, 100)
    vetor2.append(n1)
    vetor3.append(n)
    vetor3.append(n1)
print(f"vetor 1: {vetor1}")
print(f"vetor 2: {vetor2}")
print(f"vetor 3: {vetor3}")
print("-------------------------------------------------------")

##EXERCÍCIO 4:

texto = ("""The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.""")
lista = []
texto = texto.lower()
texto = texto.replace('.', ' ',).replace(',', ' ').replace(':', ' ')
texto = texto.split()

for x in texto:
    if x[0] in 'python' or x[-1] in 'python':
        lista.append(x)
print(lista)
print("-------------------------------------------------------")

##EXERCÍCIO 5:

texto = ("""The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.""")

texto = texto.lower()
texto = texto.replace('.', ' ',).replace(',', ' ').replace(':', ' ')
texto = texto.split()

print("""Digite a função cont(texto) para saber quantas palavras no texto contém
     mais de 4 caracteres e possuem uma das letras python""")

def cont(texto):
    lista = []
    for x in texto:
        if x[0] in 'python' and len(x)>4 or x[-1] in 'python' and len(x)>4:
            lista.append(x)
    a = len(lista)
    print(f"As palavras são: {lista}")
    print(f"São: {a} palavras")
print("-------------------------------------------------------")
            
             




            
        
        
















    




       
        
