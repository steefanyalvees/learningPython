import os


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

def listar_restaurantes(): 
    print('lista de restaurantes')

def cadastar_restaurantes():
    print('vamos cadastrar restaurantes')

def ativar_restaurantes():
    print('ativar restaurantes')


def escolher_opcao():
    opcao_escolhida = int(input('selecione uma opcao: ')) # colocaos o int pq vamos receber um int 
    if opcao_escolhida == 1:
        cadastar_restaurantes()   
    elif opcao_escolhida == 2:
        listar_restaurantes()
    elif opcao_escolhida == 3:
        ativar_restaurantes()
    elif opcao_escolhida == 4:
        finalizar_app()
    else:
        finalizar_app()

def main():
    exibir_nome_do_programa()
  
if __name__ == '__main__': # fazendo o main principal
    main()
    mostrar_menu()
    escolher_opcao()

    