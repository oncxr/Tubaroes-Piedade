# crm.py by Carlos (oncxr)

# Função que coleta os dados do cliente
def coletar_dados():
    nome_cliente = input("Digite seu nome:  ")

    consumo_total = 0

    # Pede o valor individual mês por mês
    for i in range(1, 13):
        while True:
            try:
                valor = float(input(f"Digite o consumo do mês {i} (em kWh):  "))
                if valor < 0:
                    # se for menor que zero, dá inválido e volta
                    print("Erro: O consumo não pode ser negativo. Tente novamente.")
                else:
                    consumo_total += valor
                    break
            except ValueError:
                print("Erro: Por favor, digite um número válido.")

    media_consumo = consumo_total / 12

    # Pede o HSP
    while True:
        try:
            hsp = float(input("Digite o HSP (Horas de Sol Pleno)"))
            if hsp <= 0:
                # Se for zero ou menor, dá inválido e volta
                print(
                    "Erro: 0 HSP deve ser maior que zero para evitar divisões inválidas."
                )
            else:
                break
        except ValueError:
            print("Erro: Por Favor, digite um número válido para o HSP")

    while True:
        try:
            preco_painel = float(input("Digite o valor da placa: "))
            if preco_painel <= 0:
                print(
                    "Erro: O preço do painel deve ser maior que zero para evitar divisões inválidas."
                )
            else:
                break
        except ValueError:
            print("Erro: Por Favor, digite um número válido para o preço do painel")

    potencia_painel = float(input("Digite a potência do painel (W): "))
    tarifa = float(input("Digite a tarifa da rua: "))
    inversor = float(input("Digite o valor do inversor: "))
    mao_obra = float(input("Digite o valor da mão de obra: "))

    return (
        nome_cliente,
        media_consumo,
        hsp,
        preco_painel,
        potencia_painel,
        tarifa,
        inversor,
        mao_obra,
    )
