from cadastro import cadastro
from login import login
from recuperacao import recuperacao
import json 

def menu():
    with open('usuario.json', 'r') as arquivo:
        contas = json.load(arquivo)

    while True:
        print('\nMENU')
        print('1 - Cadastro:' )
        print('2 - Login:')
        print('3 - Recuperar senha:')
        print('0 - Sair.')

        escolha = input('Digite um número: ')
        if escolha == '1':
            resultado = cadastro(contas)
            if resultado:
                email_cadastrado, senha_cadastrada = resultado
                contas.append([email_cadastrado, senha_cadastrada])
                with open('usuario.json', 'w') as arquivo:
                    json.dump(contas, arquivo, indent=4)
                    print('Conta realizada com sucesso!')

        elif escolha == '2':
            if not contas:
                print('Nenhum usúario cadastrado.')
                continue
            tentativas = 0
            while True:
                resultado = login(contas)
                if resultado:
                    break
                tentativas += 1
                if tentativas == 3:
                    print('Acesso bloqueado.')
                    break
                print('Vamos tentar novamente.')
        elif escolha == '3':
            recuperacao(contas)
        elif escolha == '0':
            print('Saindo...')
            break
        else:
            print('Opção invalida!')

menu()