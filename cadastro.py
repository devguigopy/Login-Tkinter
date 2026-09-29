

import hashlib
import re
from email import validar_email
from captcha import gerar_captcha, verificar_captcha
from senha import senha_com_asterisco

def cadastro(contas):
    print('Sistema de cadastro.')

    email = input('E-mail: ')
    if validar_email(email):
        print('E-mail válido.')
    else:
        print('E-mail inválido!')
        return False
    
    for usuario in contas:
        if usuario[0] == email:
            print('Esse e-mail está vinculado á uma conta.')
            return False

    senha = senha_com_asterisco()
    while True:
        tem_tamanho = len(senha) >= 8
        tem_maiuscula = bool(re.search(r'[A-Z]', senha))
        tem_minuscula = bool(re.search(r'[a-z]', senha))
        tem_numero = bool(re.search(r'[0-9]', senha))
        tem_simbolo = bool(re.search(r'[^A-Za-z0-9]', senha))

        indicador = sum([
            tem_tamanho,
            tem_maiuscula,
            tem_minuscula,
            tem_numero,
            tem_simbolo])
        if indicador <= 2:
            clas = 'Senha fraca'
        elif indicador <= 4:
            clas = 'Senha média'
        else:
            clas = 'Ótima senha'

        print('✓' if tem_tamanho else 'x', 'Pelo menos 8 caracteres.')
        print('✓' if tem_maiuscula else 'x', 'Contém uma letra maiúscula.')
        print('✓' if tem_minuscula else 'x', 'Contém uma letra minúscula.')
        print('✓' if tem_numero else 'x', 'Contém números.')
        print('✓' if tem_simbolo else 'x', 'contém algum símbolo.')
        
        if clas == 'Senha fraca':
            print('x Senha fraca!')
            senha = senha_com_asterisco()
            continue
        break

    while True:
        confirmacao = senha_com_asterisco()
        if confirmacao == senha:
            print('Senhas correta.')
            break
        else:
            print('Senha incorreta!')

    captcha = gerar_captcha()
    if not verificar_captcha(captcha):
        return False

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    return email, senha_hash

