import random
import string

def gerar_captcha():
    caracteres = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(caracteres) for _ in range(6))
    print(f'Captcha: {captcha}')
    return captcha

def verificar_captcha(captcha):
    resposta = input('Digite o CAPTCHA: ')
    if resposta == captcha:
        print('CAPTCHA correto.')
        return True
    print('CAPTCHA incorreto.')
    return False
