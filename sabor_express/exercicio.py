class music:    
    nome = ''
    artista = ''
    duracao = int


musica1 = music() # instanciando como no java
#musica1.artista('ff')
musica1.duracao(65)
#musica1.nome('hello, its me')

musica2 = music()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183


class Restaurante:
    nome = ''
    produto = ''
    preco = int
    ativo = False
    

restaurante_praca = Restaurante()
restaurante_praca.nome = "italiana"
restaurante_praca.ativo = False

# Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
nome_do_restaurante = restaurante_praca.nome
if restaurante_praca == True:
    print(" it is working")
else:
    print(" nope ")

