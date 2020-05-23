##LISTA DE EXERCÍCIOS 2:


##EXERCÍCIO 1:

print("informe os lados dos triangulos: ")
a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

if a + b < c or a + c < b or b + c < a or b + a < c:
    print ('Os valores não correspondem a um triangulo')
elif a == b == c:
    print('Corresponde a um triangulo Equilátero')
elif a == b or b == c or a ==c:
    print('Corresponde a um triangulo Isósceles')
else:
    print('Corresponde a um triangulo Escaleno')
print("-------------------------------------------------------")

##EXERCÍCIO 2:

ano = int(input("Informe o ano: "))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 ==0):
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')
print("-------------------------------------------------------")


##EXERCÍCIO 3:

peso = int(input("Informe o peso: "))
excesso = peso-50
multa = (excesso)*4
if peso > 50:
    print(f"O excesso foi de: {excesso}kg, e a multa a ser paga é de: R${multa}")
else:
    print(f"O excesso foi de: {excesso}kg, e a multa a ser paga é de: R${multa}")
print("-------------------------------------------------------")

##EXERCÍCIO 4:

valor1 = int(input("Informe o primeiro número: "))
valor2 = int(input("Informe o segundo número: "))
valor3 =int(input("Informe o terceiro número: "))
if valor1 > valor3 and valor1 > valor2:
    print(f"O maior número é o primeiro: {valor1}")
elif valor2 > valor3 and valor2 > valor1:
    print(f"O maior número é o segundo: {valor2}")
elif valor3 > valor2 and valor3 > valor1:
    print(f"O maior número é o terceiro: {valor3}")
else:
    print("Os números são iguais")
print("-------------------------------------------------------")

##EXERCÍCIO 5:

valor1 = int(input("Informe o primeiro número: "))
valor2 = int(input("Informe o segundo número: "))
valor3 =int(input("Informe o terceiro número: "))
if valor1 > valor3 and valor1 > valor2:
    print(f"O maior número é o primeiro: {valor1}")
elif valor2 > valor3 and valor2 > valor1:
    print(f"O maior número é o segundo: {valor2}")
elif valor3 > valor2 and valor3 > valor1:
    print(f"O maior número é o terceiro: {valor3}")
if valor1 < valor2 and valor1 < valor3:
    print(f"O menor número é o primeiro: {valor1}")
elif valor2 < valor1 and valor2 < valor3:
    print(f"O menor número é o segundo: {valor2}")
elif valor3 < valor2 and valor3 < valor1:
    print(f"O menor número é o terceiro: {valor3}")
else:
    print("Os números são iguais")
print("-------------------------------------------------------")

##EXECÍCIO 6:

salario_hora = float(input("Informe quanto você ganha por hora: "))
horas_trabalhadas = int(input("Informe quantas horas você trabalha por mês: "))
salario_bruto = salario_hora * horas_trabalhadas
print(f"Salário bruto: R${salario_bruto}")
ir = (salario_bruto*11)/100
print(f"Imposto de renda (11%): R${ir}")
inss = (salario_bruto*8)/100
print(f"INSS(8%): R${inss}")
sind = (salario_bruto*5)/100
print(f"Sindicato(5%): R${sind}")
descontos = (ir+inss+sind)
print(f"Os descontos do seu salário são de: R${descontos}")
salario_liquido = salario_bruto-descontos
print(f"Salário liquido: R${salario_liquido}")
print("-------------------------------------------------------")
        

##EXERCÍCIO 7:

metros = int(input("Informe o tamanho em metros quadrados da área a ser pintada: "))
litro = int(metros*3)
lata = int(litro/18)
lata2 = int(litro/18)+1
valor_lata = int(lata*80)
valor_lata2 = int(lata2*80)
if litro <= 18:
    print(f"Você terá de comprar 1 lata de tinta (18 litros) no valor de: R$80.00")
elif litro > 18 and litro > (18*lata):
    print(f"Você usará {litro} litros de tinta")
    print(f"Você terá de comprar {lata2} latas de tinta(18 litros)")
    print(f"No valor de: R${valor_lata2}.00")
else:
    print(f"Você usará {litro} litros de tinta")
    print(f"Você terá de comprar {lata} latas de tinta(18 litros)")
    print(f"No valor de: R${valor_lata}.00")
print("-------------------------------------------------------")







    
           






