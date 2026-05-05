nome_cliente = input("Digite seu nome de usuário:  ")
consumo_total= 0
for i in range(1, 13):
    while True:
        try:
            valor = float(input(f"Digite o consumo do mês {i} (em kWH:  "))
            if valor < 0:
                print("Erro: 0 consumo não pode ser negativo. Tente novamente.")
            else:
                consumo_total += valor
                break
        except ValueError:
            print("Erro: Por favor, digite um número válido.")
            
media_consumo = consumo_total / 12

while True:
    try:
        hsp = float(input("Digite o HSP (Horas de Sol Pleno)"))
        if hsp <= 0:
            print("Erro: 0 HSP deve ser maior que zero para evitar divisões inválidas.")
        else:
            break
    except ValueError:
        print("Erro: Por Favor, digite um número válido para o HSP")
print("-" * 30)
print(f"Relátorio de Coleta - Cliente: {nome_cliente}")
print(f"Consumo Total Anual: {consumo_total} kWh")
print(f"Média Mensal de Consumo: {media_consumo:} kWh")
print(f"HSP Informado: {hsp:}")
print("- * 30")
