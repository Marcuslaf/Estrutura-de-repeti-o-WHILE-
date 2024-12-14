while True: # Laço para garantir entrada válida
    try:
        numero = int(input("Digite um número entre 1 e 10: ")) # Solicite entrada do usuário
        
        if 1 <= numero <= 10: # Verifica se o número está no intervalo válido
            print(f"Você digitou o número {numero}. Entrada válida!") # Número válido, interrompe o laço
            break 
        else:
            print("Erro: O número deve estar entre 1 e 10.") # Número fora do intervalo
    
    except ValueError: # Usado quando não é atendido o que foi solicitado.
        print("Erro: Por favor, digite um número inteiro.")