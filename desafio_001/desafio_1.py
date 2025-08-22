# dados de vendas da semana
vendas = {
    "segunda": 1250.50,
    "terca": 980.25,
    "quarta": 1450.50,
    "quinta": 1100.00,
    "sexta": 2100.80,
    "sabado": 1800.90,
    "domingo": 1350.30
}

# calculando o valor total em vendas da semana
total_vendas = sum(vendas.values())
print(f'Total de vendas: {total_vendas}')

# obtendo a maior venda da semana
maior_venda = max(vendas.values())
print(f'Maior venda: {maior_venda}')

# obtendo o menor venda da semana
menor_venda = min(vendas.values())
print(f'Menor venda: {menor_venda}')

# calculando a média de vendas, por dia na semana
media_venda = total_vendas / len(vendas)
print(f'Media venda por dia: {media_venda:.2f}')