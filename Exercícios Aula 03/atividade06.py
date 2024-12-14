soma = 0 # Inicializa a variável para armazenar a soma

while True:
    numero = float(input("Digite um número (número negativo para encerrar): ")) # Solicite um número ao usuário
    
    if numero < 0: # Verifica se o número é negativo
        break
    
    soma += numero # Adiciona o número positivo à soma

print(f"A soma dos números positivos é: {soma}")