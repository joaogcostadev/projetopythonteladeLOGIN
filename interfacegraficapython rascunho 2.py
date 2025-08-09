#sistema de login 

import customtkinter as ctk
ctk.set_appearance_mode("light") # modo claro
ctk.set_default_color_theme("blue") # tema azul

def.validar_login():
usuario=entry_usuario.get()
    senha=entry_senha.get()
    if usuario == 'joaocosta' and senha == '12345':
        resultado_login.configure(text='login bem sucedido', text_color='green')
    else:
        resultado_login.configure(text='login falhou', text_color='red')


# aparencia tela inicial titulo e tamanho
app = ctk.CTk()
app.title("Sistema de Login")
app.iconbitmap("login.ico") # icone da janela
 
app.geometry("400x300")
#label 1 cria o label de titulo
#entry 2 cria o campo de entrada para o usuario
#label 1
#entry 2
#button por ultimo fim cria o botao de login
label_usuario=ctk.CTkLabel(app,text='Usuario')
label_usuario.pack(pady=10) # adiciona o label na tela com espaçamento vertical
label_usuario.pack(pady=10)

#entry 2
# cria o campo de entrada para o usuario
entry_usuario=ctk.CTkEntry(app,placeholder_text='digite seu usuario')
entry_usuario.pack(pady=10)

senha_campo=ctk.CTkLabel(app,text='Senha') # cria o label de senha
senha_campo.pack(pady=20)
entry_senha=ctk.CTkEntry(app,placeholder_text='digite sua senha')
entry_senha.pack(pady=10)
#button por ultimo fim cria o botao de login
botao_login=ctk.CTkButton(app,text='LOGIN',command=validar_login) # cria o botao de login
botao_login.pack(pady=20)

resultado_login=ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)

app.mainloop()