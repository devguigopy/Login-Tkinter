# Login Tkinter

Sistema de cadastro, login e recuperação de senha desenvolvido em Python.

> Projeto pessoal desenvolvido com foco em prática de lógica de programação,
> organização de código, autenticação e persistência de dados.

## 📌 Sobre o projeto

O projeto começou como um sistema de autenticação executado pelo terminal,
com o objetivo de praticar conceitos fundamentais de Python.

Atualmente o sistema possui:

- Cadastro de usuários
- Validação de e-mail
- Validação de senha
- Confirmação de senha
- Hash de senha com SHA-256
- Login de usuários
- CAPTCHA
- Recuperação de senha
- Código de recuperação
- Alteração de senha
- Persistência dos usuários em arquivo JSON
- Proteção da senha durante a digitação
- Controle de tentativas de login

A interface gráfica com Tkinter será desenvolvida em uma etapa posterior.

---

## 🚀 Funcionalidades

### Cadastro

O sistema permite criar uma nova conta utilizando um endereço de e-mail
válido e uma senha que atende aos requisitos definidos pelo projeto.

A senha deve possuir:

- Pelo menos 8 caracteres
- Uma letra maiúscula
- Uma letra minúscula
- Um número
- Um caractere especial

O sistema também verifica se o e-mail já está cadastrado.

### Login

O usuário informa seu e-mail, resolve o CAPTCHA e digita sua senha.

A senha informada é transformada em um hash SHA-256 antes de ser comparada
com o valor armazenado no sistema.

O login possui limite de tentativas.

### Recuperação de senha

O usuário pode solicitar a recuperação informando seu e-mail cadastrado.

O sistema:

1. Verifica se o e-mail é válido.
2. Procura a conta cadastrada.
3. Gera um código de recuperação.
4. Simula o envio do código.
5. Solicita o código ao usuário.
6. Permite definir uma nova senha.
7. Atualiza a senha armazenada no arquivo JSON.

> Atualmente o envio do código é simulado no terminal. O envio real por
> e-mail será implementado posteriormente.

### Proteção da senha

Durante a digitação, a senha não é exibida diretamente no terminal.

Exemplo: ```text
Senha: ********

### Estrutura do projeto

Login-tkinter/
|
|--assets/
|--relatorios/
|
|--cadstro.py
|--captcha.py
|--email.py
|--login.py
|--main.py
|--recuperacao.py
|--senha.py
|--usuario.json
|--requirments.txt
|--README.md

### Principais arquivos

> main.py => Controla o menu principal e o fluxo do sistema.
> cadastro.py => Realiza o cadastro de usuários.
> login.py => Realiza a autenticação.
> recuperacao.py => Controla a recuperação e alteração de senha.
> senha.py => Gerencia a entrada mascarada de senhas.
> captcha.py => Gera e verifica o CAPTCHA.
> email.py => Valida e-mails e simula o envio do código.
> usuario.json => Armazena os dados dos usuário.
> requirements.txt => Lista as dependências do projeto.
> relatorios/ => Guarda os registro do desenvolvimento.

### Tecnologias ultilizadas

- Python 3
- JSON
- hashlib
- re
- random
- string
- sys
- termios
- tty

### Como executar

Clone o projeto:
	git clone URL_DOREPOSITORIO

Entre na pasta:
	cd login-tkinter

Execute o sistema:
	python3 main.py
	
### Segurança

O projeto ultiliza SHA-256 para armazenar uma representação criptográfica das senhas em vez de armazená-las em texto puro.
As senhas também sçao ocultadas durante a digitação.

> Este projeto possui finalidade educacional. Para uma aplicação real, seriam necessárias medidas adicionais de segurança, como armazenamento seguro de segredos, gereciamento adequado de credeciais, mecanismos de recuperação de conta mais robustos e um algoritmo de armazenamento de senha apropriado para produção.

# Status do projeto

### Concluído

- [x] Cadastro
- [x] LOgin
- [x] Hash de senhas
- [x] Entrada
- [x] CAPTCHA
- [x] Recuperação de senha
- [x] Persistência em JSON
- [x] Validaçãio centralizada de e-mail
- [x] Testes dos principais fluxos

### Próximos passos

- [] Revisar documentação
- [] Finalizar requirements.txt
- [] Publicar no GitHub
- [] Desenvolver interface gráfica com Tkinter
- [] Substituir o envio simulado por envio real de e-mail

## Objetivo

Este projeto faz parte do meu apredizado em desenvolvimento de software e tem como objetivo praticar:

- Python
- Lógica de programação
- Modularização
- Persistência de dados
- Autenticação
- Organização de projeto
- Git e GitHub

### Autor

> Projeto pessoal desenvolvido para estudos e construção de portifólio.
