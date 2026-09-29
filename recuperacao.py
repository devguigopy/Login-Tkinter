import json
import random
import hashlib
from senha import senha_com_asterisco
from email import validar_email, enviar_codigo

def recuperacao(contas):
    print('Sistema de recuperação de senha.')
    with open('usuario.json', 'r') as arquivo:
        contas = json.load(arquivo)

    email = input('Digite seu e-mail: ')
    if not validar_email(email):
        print('E-mail inválido.')
        return False

    usuario_encontrado = None
    for usuario in contas:
        if usuario[0] == email:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        print('E-mail não encontrado.')
        return

    codigo = str(random.randint(100000, 999999))
    enviar_codigo(email, codigo)
    codigo_digitado = input('Digite o código: ')
    if codigo_digitado != codigo:
        print('Código incorreto.')
        return
    print('Código correto.')

    nova_senha = senha_com_asterisco()
    confirmacao = senha_com_asterisco()
    if nova_senha != confirmacao:
        print('As senhas não coicidem.')
        return
    
    senha_hash = hashlib.sha256(nova_senha.encode()).hexdigest()
    usuario_encontrado[1] = senha_hash
    with open('usuario.json', 'w') as arquivo:
        json.dump(contas, arquivo, indent=1)
    print('Senha alterada com sucesso!')
