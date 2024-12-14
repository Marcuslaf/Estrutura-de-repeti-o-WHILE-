numero = int(input("Digite um número: ")) # Solicite um número ao usuário

contador = 1 # Inicializa o contador

# Laço while para exibir os números ímpares de 1 até o número inserido
while contador <= numero:
    if contador % 2 != 0:  # Verifica se o número é ímpar
        print(contador)    # Exibe o número ímpar
    contador += 1          # Incrementa o contador