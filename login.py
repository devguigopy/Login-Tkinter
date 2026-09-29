import sys
import termios
import tty
import hashlib
from captcha import gerar_captcha, verificar_captcha
from senha import senha_com_asterisco
    
def login(contas):
    print('Sistema de login.')

    email = input('E-mail: ')

    if (
        email.endswith('@gmail.com') or 
        email.endswith('@yahoo.com') or 
        email.endswith('@hotmail.com')
        ):
        print('E-mail valido')
    else:
        print('E-mail invalido!')
        return False 


    captcha = gerar_captcha()
    if not verificar_captcha(captcha):
        return False
    

    senha = senha_com_asterisco()
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()
    for usuario in contas:
        if usuario[0] == email:
            if usuario[1] == senha_hash:
                print('Acessando conta.')
                print('Aguarde um momento...')
                return True
            else:
                print('Acesso negado! Senha ou e-mail incorreto.')
                return False
    print('Acesso negado! Senha ou e-mail incorreto.')
    return False