import sys
import termios
import tty

def senha_com_asterisco():
    senha = ''
    print('Senha: ', end='', flush=True)
    fd = sys.stdin.fileno()
    configuracao = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            caractere = sys.stdin.read(1)
            if caractere in ('\n', '\r'):
                break
            if caractere in ('\x7f', '\x08'):
                if senha:
                    senha = senha[:-1]
                    print('\b \b', end='', flush=True)
            else:
                senha += caractere
                print('*', end='', flush=True)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, configuracao)
    print()
    return senha