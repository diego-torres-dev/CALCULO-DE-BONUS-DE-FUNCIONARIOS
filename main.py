# Importa a biblioteca locale
import locale

# Define o local
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

# Valor total das vendas de cada funcionário
vendas_funcionario1 = 10_000
vendas_funcionario2 = 7_700
vendas_funcionario3 = 27_000
vendas_funcionario4 = 15_000


def calcular_bonus(vendas_funcionario):
    """Calcula o bônus que o funcionário receberá com base no valor total de suas vendas

        Parâmetro:
            vendas_funcionarios (float): valor das vendas do funcionário

        Retorna:
            bonus_funcionario (float): retorna o valor do bônus do funcionário
    """

    if vendas_funcionario >= 20_000:
        bonus_funcionario = vendas_funcionario * 0.15
    elif vendas_funcionario >= 10_000:
        bonus_funcionario = vendas_funcionario * 0.10
    else:
        bonus_funcionario = 0

    return locale.currency(bonus_funcionario, grouping=True)


# Exibição dos resultados
print(f"Bônus funcionário 1: {calcular_bonus(vendas_funcionario1)}")
print(f"Bônus funcionário 2: {calcular_bonus(vendas_funcionario2)}")
print(f"Bônus funcionário 3: {calcular_bonus(vendas_funcionario3)}")
print(f"Bônus funcionário 4: {calcular_bonus(vendas_funcionario4)}")
