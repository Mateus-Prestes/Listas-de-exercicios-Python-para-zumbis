##LISTA DE EXERCÍCIOS 3:

##EXERCÍCIO 1:

nota = int(input("Informe a nota de 0 a 10: "))

while nota < 0 or nota > 10:
    print("Valor inválido")
    print("----------------")
    nota = int(input("Informe a nota de 0 a 10: "))
else:
    print("Nota válida")
print("-------------------------------------------------------")

##EXERCÍCIO 2:

user = str(input("Iforme o usúario: "))
key = str(input("Informe a senha: "))
while user == key:
    print("ERRO")
    print("----------------")
    user = str(input("Iforme o usúario: "))
    key = str(input("Informe a senha: "))
else:
    print("Usúario e senha definidos")
print("-------------------------------------------------------")

##EXERCÍCIO 3:

a = 80000
b = 200000
c = 0
while a < b:
    porcentagem_a = (a * 3)/100
    porcentagem_b = (b * 1.5)/100
    a = a + porcentagem_a
    b = b + porcentagem_b
    c = c + 1
    if a > b:
        break
print("A população 'a' precisou de %d anos para passar a população 'b'" %c)
print("-------------------------------------------------------")

##EXERCÍCIO 4:

n = int(input("Insira o número: "))
a = 1
b = 1
cont = 1
while cont <= n - 2:
    b = a + b
    a = b - a
    cont = cont + 1
print(f"Fibonacci ({n}) = {b}")
print("-------------------------------------------------------")

##EXERCÍCIO 5:

n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))
resto = (n1 % n2)
resto1 = (n1 % n2)
cont = 1
while cont == 1:
    if resto != 0:
        resto = n2%resto
        n2 = resto
        if resto == 0:
            print(f"O MDC dos números é: {resto1}")
        else:
            print(f"O MDC dos números é: {resto}")
    elif resto == 0:
        print(f"O MDC dos números é: {n2}")
    cont = cont + 1
print("-------------------------------------------------------")
        
    
    
    
    
