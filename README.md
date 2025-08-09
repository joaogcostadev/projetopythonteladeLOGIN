# Projeto de login python basico

Bem-vindo ao meu primeiro projeto de login desenvolvido em Python! Este repositório é uma prática que busquei para aprimorar minhas habilidades de programação e aprender mais sobre a criação de interfaces gráficas.

Python: A linguagem de programação escolhida para desenvolver o projeto.
CustomTkinter: Biblioteca utilizada para criar a interface gráfica do usuário.

Sistema de Login: Um formulário simples onde os usuários podem inserir seu nome de usuário e senha.
Validação de Credenciais: O sistema verifica se as credenciais correspondem às informações pré-definidas.
Feedback Visual: Mensagens de sucesso ou erro são exibidas dependendo do resultado do login.

Funcionalidades = o programa vai dar o resultado de login correto apenas se digitar usuario:joaocosta senha:12345
ao contrario ele resultada em login incorreto
foi feito a partir de um configure + a variavel se usuario joaocosta== e senha 12345 
|
 usuario = entry_usuario.get()
    senha = entry_senha.get()
    if usuario == 'joaocosta' and senha == '12345':
        resultado_login.configure(text='login bem sucedido', text_color='green')
    else:
        resultado_login.configure(text='login falhou', text_color='red')
|  




## feito por:

- [@joaogcostadev](https://www.github.com/joaogcostadev)
