def validar_email(email):
    dominios_validos = (
        '@gmail.com',
        '@yahoo.com',
        '@hotmail.com'
    )
    return email.endswith(dominios_validos)

def enviar_codigo(email, codigo):
    print(f'Código enviado para {email}.')
    print(f'Código: {codigo}')
