import pandas as pd
import numpy as np

# Criando dataset estruturado
dados_vendas = {
    'filial': ['SP1', 'SP1', 'SP1', 'RJ1', 'RJ1', 'RJ1', 'MG1', 'MG1', 'MG1', 
               'SP2', 'SP2', 'SP2', 'RJ2', 'RJ2', 'RJ2', 'MG2', 'MG2', 'MG2',
               'SP3', 'SP3', 'SP3', 'RS1', 'RS1', 'RS1'],
    'produto': ['Eletrônicos', 'Roupas', 'Casa'] * 8,
    'trimestre': ['Q1', 'Q2', 'Q3'] * 8,
    'vendas': [12500, 15800, 9200, 18900, 11400, 16700, 8900, 14300, 13800, 
               16200, 11500, 17800, 12900, 17100, 10200, 16400, 15200, 13900,
               14500, 16800, 11200, 19200, 12800, 15600],
    'meta': [12000] * 24,
    'custos': [8750, 11060, 6440, 13230, 7980, 11690, 6230, 10010, 9660, 
               11340, 8050, 12460, 9030, 11970, 7140, 11480, 10640, 9730,
               10150, 11760, 7840, 13440, 8960, 10920]
}

# print(dados_vendas)

df = pd.DataFrame(dados_vendas)
print("Dataset shape:", df.shape)
print("\nPrimeiras linhas:")
print(df.head())

# Passo 2: Informações básicas do dataset
print("\nInfo do dataset:")
print(df.info())
print("\nEstatísticas descritivas:")
print(df.describe())

# Passo 3: Análise por agrupamentos
print("\nVendas por filial:")
vendas_por_filial = df.groupby('filial')['vendas'].agg(['mean', 'sum', 'count'])
print(vendas_por_filial)

print("\nVendas por produto:")
vendas_por_produto = df.groupby('produto')['vendas'].mean().sort_values(ascending=False)
print(vendas_por_produto)

# Passo 4: Análise de performance
df['lucro'] = df['vendas'] - df['custos']
df['margem_lucro'] = (df['lucro'] / df['vendas']) * 100
df['atingiu_meta'] = df['vendas'] >= df['meta']

print(f"\nPercentual que atingiu meta: {df['atingiu_meta'].mean()*100:.1f}%")
print(f"Lucro médio: {df['lucro'].mean():.2f}")
print(f"Margem de lucro média: {df['margem_lucro'].mean():.2f}%")

# Passo 5: Identificar outliers
q1 = df['vendas'].quantile(0.25)
q3 = df['vendas'].quantile(0.75)
iqr = q3 - q1
outliers = df[(df['vendas'] < q1 - 1.5*iqr) | (df['vendas'] > q3 + 1.5*iqr)]

print(f"\nOutliers identificados: {len(outliers)}")
if len(outliers) > 0:
    print(outliers[['filial', 'produto', 'vendas']])