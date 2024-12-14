# Inicializa variáveis
numero_atual = 1  # Primeiro número a ser somado
soma_total = 0    # Acumulador da soma

while soma_total < 50: # Laço while para somar números consecutivos
    soma_total += numero_atual # Adiciona o número atual à soma
    
    print(f"Número somado: {numero_atual}, Soma total: {soma_total}")
    
    numero_atual += 1 # Incrementa para o próximo número

# Resultado final
print(f"\nÚltimo número somado: {numero_atual - 1}")
print(f"Soma final: {soma_total}")