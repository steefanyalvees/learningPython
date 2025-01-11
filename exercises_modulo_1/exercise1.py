#1 - Crie uma lista para cada informação a seguir:

#Lista de números de 1 a 10;
list_number = [1,2,3,4,5,6,7,8,9,10]
#Lista com quatro nomes;
lista_name =['Ste', 'Le']
#Lista com o ano que você nasceu e o ano atual.
lista_year = [1997,1990]
print(list_number, lista_name, lista_year)

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
numeros = [1,2,3,4,5]
for numero in numeros:
    print(f'{numeros}')

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
numero_impar = [1, 3, 5, 7, 9]
for numero in numero_impar:
    print (numero_impar)
   # numero_impar.append

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
numero_impar = [1,3,5,7,9]
for numero in numero_impar:
   print (numero_impar)

#outro array example nome

name = ['stefany','leandro', 'jeni']
for nome in name:
    print(name)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número,
#  indo de 1 a 10.
numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):#Esse for cria um loop que vai de 1 a 10 (inclusive), e o i recebe esse valor
    resultado = numero_tabuada * i # para cada valor de i, o programa calcula o produto de numero_tabuada  e i
    print(f"{numero_tabuada} x {i} = {resultado}")


tabuadas_resultados = int(input(' ola digite numero para a tabuada '))
for i in range(10,21):
    calcular_resultado = tabuadas_resultados * i
    print(f'{tabuadas_resultados} x {i} = {calcular_resultado}')

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.

numeros_lista = [1,8,9,3,7,1,2]
soma = 0 # soma é inicializada com o valor 0. Ela será usada para armazenar o somatório dos números da lista.
for numero in numeros_lista:
    soma += numero # O operador += soma o valor de numero à variável soma
print(soma)
