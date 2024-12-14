numero = int(input("Digite um número para ver a tabuada: ")) # Solicite um número ao usuário

multiplicador = 1 # Inicializa o contador


while multiplicador <= 10: # Laço while para gerar a tabuada de 1 a 10
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")  # Exibe o resultado
    multiplicador += 1  # Incrementa o multiplicador