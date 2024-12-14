senha_correta = "python123" # Definição da senha correta


while True: # Laço para validação de senha
    
    senha_digitada = input("Digite a senha: ") # Solicite senha ao usuário
    
    if senha_digitada == senha_correta: # Verifica se a senha está correta
        print("Acesso concedido!")
        break
    else:
        print("Senha incorreta. Tente novamente.")