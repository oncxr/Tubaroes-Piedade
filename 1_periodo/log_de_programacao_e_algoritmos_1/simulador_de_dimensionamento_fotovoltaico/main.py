from crm import coletar_dados
from motor_solar import calc_consumo_diario, calc_kwp, calc_paineis


def main():
    print("--- SIMULADOR FOTOVOLTAICO ---")

    nome_cliente, consumo_mensal, hsp = coletar_dados()

    potencia_painel = float(input("Digite a potência do painel (W): "))

    consumo_diario = calc_consumo_diario(consumo_mensal)
    kwp_total = calc_kwp(consumo_diario, hsp)
    qtd_paineis = calc_paineis(kwp_total, potencia_painel)

    if qtd_paineis is None:
        print("Erro no cálculo dos painéis.")
        return

    custo_total = qtd_paineis * potencia_painel * 4.50
    economia_mensal = consumo_mensal * 0.95
    payback_anos = custo_total / (economia_mensal * 12)

    # 5. Resultado
    print("\n" + "-" * 40)
    print(f"Cliente: {nome_cliente}")
    print("=" * 40)
    print(f"Consumo médio mensal: {consumo_mensal} kWh")
    print(f"Consumo diário: {consumo_diario} kWh")
    print(f"Potência necessária: {kwp_total} kWp")
    print(f"Quantidade de painéis: {qtd_paineis}")
    print(f"Custo estimado: R$ {custo_total:.2f}")
    print(f"Payback estimado: {payback_anos:.2f} anos")
    print("-" * 40)


main()
