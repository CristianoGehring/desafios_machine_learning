import numpy as np

# Passo 1: Criar arrays NumPy
vendas_q1 = np.array([12500, 15800, 9200, 18900, 11400, 16700, 8900, 14300])
vendas_q2 = np.array([14200, 17500, 10800, 19400, 13100, 18200, 9600, 15800])
vendas_q3 = np.array([13800, 16200, 11500, 17800, 12900, 17100, 10200, 16400])

# Passo 2: Operações vectorizadas (SEM loops!)
todas_vendas = np.array([vendas_q1, vendas_q2, vendas_q3])
print(todas_vendas.shape)

# Médias por trimestre (axis=1) e por filial (axis=0)
media_por_trimestre = np.mean(todas_vendas, axis=1)
media_por_filial = np.mean(todas_vendas, axis=0)

print(f"Médias por trimestre: {media_por_trimestre}")
print(f"Médias por filial: {media_por_filial}")

# Passo 3: Broadcasting - comparar cada filial com média geral
media_geral = np.mean(todas_vendas)
print(f"Média geral: {media_geral:.2f}")

performance_relativa = todas_vendas - media_geral  # Broadcasting!
print(f"Performance relativa:\n{performance_relativa}")

# Passo 4: Normalização (preparação para ML)
vendas_normalizadas = (todas_vendas - np.mean(todas_vendas)) / np.std(todas_vendas)

# Passo 5: Correlação entre trimestres
correlacao_q1_q2 = np.corrcoef(vendas_q1, vendas_q2)[0, 1]
print(f"Correlação Q1-Q2: {correlacao_q1_q2:.3f}")
correlacao_q1_q3 = np.corrcoef(vendas_q1, vendas_q3)[0, 1]
print(f"Correlação Q1-Q3: {correlacao_q1_q3:.3f}")
correlacao_q2_q3 = np.corrcoef(vendas_q2, vendas_q3)[0, 1]
print(f"Correlação Q2-Q3: {correlacao_q2_q3:.3f}")