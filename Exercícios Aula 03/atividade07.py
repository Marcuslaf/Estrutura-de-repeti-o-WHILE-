numero = int(input("Digite um número para ver sua tabuada (múltiplos de 3): ")) # Solicite o número ao usuário

contador = 1 # Inicializa o contador


while contador <= 10: # Laço para percorrer de 1 a 10
    resultado = numero * contador # Calcula o resultado da multiplicação
    
    if resultado % 3 == 0: # Verifica se o resultado é múltiplo de 3
        print(f"{numero} x {contador} = {resultado}") # Imprime apenas os resultados múltiplos de 3
    
    contador += 1 # Incrementa o contador