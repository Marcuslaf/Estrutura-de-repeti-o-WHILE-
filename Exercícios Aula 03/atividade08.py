# Inicializa as variáveis para o controle da soma e contagem de notas
soma_notas = 0
quantidade_notas = 0

while True: # Estrutura de repetição para entrada de notas
    nota = float(input("Digite uma nota (ou -1 para encerrar): ")) # Solicite nota do usuário
    
    if nota == -1: # Condição de parada
        break
    
    if nota < 0 or nota > 10: # Valida entrada de notas (entre 0 e 10)
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        continue
    
    # Adiciona nota à soma e incrementa contador
    soma_notas += nota
    quantidade_notas += 1


if quantidade_notas > 0: # Verifica se foram inseridas notas
    media = soma_notas / quantidade_notas # Calcula média
    # Exibe resultados
    print(f"\nQuantidade de notas inseridas: {quantidade_notas}")
    print(f"Soma das notas: {soma_notas:.2f}")
    print(f"Média das notas: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")