import os

restaurantes = ['Pizza', 'sushi']# lista array

def exibir_nome_do_programa(): #def e uma funcao 
    print('🅢 🅐 🅑 🅞 🅡 🅔 🅢 🅟 🅡 🅔 🅢 🅢\n')

def mostrar_menu():
    print('1 - cadastrar restaurante')
    print('2 - listar restaurante')
    print('3 - Ativar  resturante')
    print('4 - sair\n')


def finalizar_app():
    os.system('cls')
    print('seu app foi finalizado')

def lista_restaurantes(): 
    os.system('cls')
    print('listando os restaurantes')

    for restaurante  in restaurantes:
        print(f'.{restaurantes }')

    input('digite uma tecla para voltar para o main')
    main()

def cadastar_restaurantes():
    os.system('cls')
    nome_do_restaurante=input('digite o nome do restaurante')
    restaurantes.append(nome_do_restaurante)
    print(f' o nome do restaurante e {nome_do_restaurante}')
    input('digite uma tecla para voltar para o main')
    main()

def ativar_restaurantes():
    print('ativar restaurantes')

def opcao_invalida():
    print('opcao invalida\n')
    input('digite 1 para voltar a tecla principal')
    main()
   

def escolher_opcao():
    try:
        opcao_escolhida = int(input('selecione uma opcao: ')) # colocaos o int pq vamos receber um int 
        if opcao_escolhida == 1:
            cadastar_restaurantes()   
        elif opcao_escolhida == 2:
            lista_restaurantes()
        elif opcao_escolhida == 3:
            ativar_restaurantes()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        ('opcao invalida ')

def main():
    os.system('cls') #limpar tela
    exibir_nome_do_programa()
  
if __name__ == '__main__': # fazendo o main principal
    main()
    mostrar_menu()
    escolher_opcao()

    