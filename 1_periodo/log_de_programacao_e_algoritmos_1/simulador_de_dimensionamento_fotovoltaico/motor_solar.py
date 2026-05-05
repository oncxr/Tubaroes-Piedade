# Função que calcula o consumo diário
def calc_consumo_diario(consumo_mensal):
    return consumo_mensal / 30

# Função que calcula o kWp
def calc_kwp(consumo_diario, hsp):
    if (hsp == 0):
        print('ERRO: Você colocou o valor zero no HSP, tente novamente com um valor maior.')
        return None
    else:
        return consumo_diario / (hsp * 0.8)

# Função que calcula os painéis
def calc_paineis(kwp_total, potencia_painel):
    resultado = kwp_total / potencia_painel

    # Aqui ele pega o resultado que mostrará a quantidade de painéis
    # Para não permitir números quebrados e se tiver, arredondar pra mais
    # O código converte o resultado para int (ex 4.3 vira 4) e compara os valores
    # Caso o resultado seja um número quebrado e seja maior que o número convertido para inteiro
    # Ele transforma o número e inteiro e acrescenta em 1
    if (resultado > int(resultado)):
        quant_paineis = int(resultado) + 1
    else:
        quant_paineis = int(resultado)

    return quant_paineis