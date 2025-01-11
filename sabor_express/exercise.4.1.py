# 3 - Crie um dicionário utilizando para representar números 
# e seus quadrados de 1 a 5.

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

#explicaccao codigo
#{}: Isso indica que estamos criando um dicionário.
#x: x**2: Aqui, x é a chave do dicionário e x**2 é o valor associado à chave x. 
# O **2 significa elevar x ao quadrado.
#for x in range(1, 6): Isso é um loop que itera sobre o intervalo de números gerado pela função range(1, 6). O range(1, 6) gera os números de 1 até 5 (o número 6 não é incluído).