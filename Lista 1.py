##LISTA DE EXERCICÍOS 1

##EXERCÍCIO 1:

valor1= int(input('digite aqui o primeiro valor: '))
valor2= int(input('digite aqui o segundo valor: '))
print(f"a soma dos valores é igual a: {valor1 + valor2} ")
print ("-------------------------------------------------------------")

##EXERCÍCIO 2:

metros = int(input("informe os metros: "))
milimetros= metros*1000
print (f"o numero de milimetros é: {milimetros}")
print ("-------------------------------------------------------------")

##EXERCÍCIO 3:

dias= int(input("informe os dias: "))
horas= int(input("informe as horas: "))
minutos= int(input("informe os minutos: "))
segundos= int(input("informe os segundos: "))
print(f"o valor esses numeros convertidos em segundos são iguais a: {(dias*24*60*60)+(horas*60*60)+(minutos*60+segundos)}")
print ("-------------------------------------------------------------")
##EXERCÍCIO 4:

salario = int(input("informe o salário: "))
porcentagem = int(input("informe a porcentagem de aumento: "))
porcentagemaumento = int((salario*porcentagem)/100)
novo = int(salario+porcentagemaumento)
print(f"a porcentagem equivale a: {porcentagemaumento}")
print(f"seu novo salário é: {novo}")
print ("-------------------------------------------------------------")

##EXERCÍCIO 5:

produto = int(input("informe o valor do produto: "))
desconto = int(input("informe a porcentagem de desconto: "))
desconto2 = int((produto*desconto)/100)
fim = int(produto-desconto)
print (f"O valor final com desconto:{fim}")
print ("-------------------------------------------------------------")

##EXERCÍCIO 6:

km = float(input("informe a distância a ser percorrida em KM pelo veículo: "))
velocidade = float(input("informe a velocidade média em KM/h esperada para a viagem: "))
kmh = float(km/velocidade)
print(f"O tempo gasto em viagem será de: {kmh}(h.min) ")
print ("-------------------------------------------------------------")

##EXERCÍCO 7:

c = float(input("informe o valor da temperatura em celcius: "))
f = float(c * float(1.8) + float(32))
print(f"o valor da temperatura informada em celcius convertida em fahrenheit é: {f}")
print ("-------------------------------------------------------------")

##EXERCÍCIO 8:

f = float(input("Informe o valor da temperatura em fahrenheit: "))
c = float(f - int(32))/1.8
print(f"O valor da temperatura informada em fahrenheit convertida para celcius é: {c}")
print ("-------------------------------------------------------------")

##EXERCÍCIO 9:

a = int(input("informe a quantidade de KM percorridos com o carro: "))
b = int(input("informe a quantidade de dias ue o carro foi alugado: "))
c = float(a*60.00)
d = float(b*0.15)
e = float(c+d)
print(f"O valor a ser pago é de : R${e}")
print ("-------------------------------------------------------------")

##EXERCÍCIO 10:

cigarros = float(input("Informe quantos cigarros você fuma por dia: "))
anos = float(input("Informe a quantos anos você fuma: "))
dias_em_anos = float(365 * anos)
minutos_perdidos = float(cigarros*10)*dias_em_anos
dias_perdidos= float(minutos_perdidos)/int(1440)

print(f"Você perdeu {dias_perdidos} dias de vida")
print ("-------------------------------------------------------------")

##EXERCÍCIO 11:

a = len(str(2**1000000))
print (f"São {a} dígitos em 2 elevado a 1 milhão")
print ("-------------------------------------------------------------")






