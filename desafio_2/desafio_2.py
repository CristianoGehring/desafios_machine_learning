# Dados de entrada
vendas_categorias = {
    "Eletrônicos": 15750.80,
    "Roupas": 8920.45,
    "Casa e Jardim": 12300.60,
    "Esportes": 6780.30,
    "Livros": 4560.90,
    "Alimentação": 18900.75,
    "Beleza": 9840.20
}

# Meta definida
meta = 10000

# Listas para agrupar desempenho
categorias_alto_desempenho = []
categorias_medio_desempenho = []
categorias_baixo_desempenho = []

# Análise de desempenho por categoria
print("🔍 Análise de Desempenho por Categoria:\n")
for categoria, valor in vendas_categorias.items():
    if valor >= meta * 1.2:
        performance = "Alto"
        categorias_alto_desempenho.append(categoria)
    elif valor >= meta:
        performance = "Médio"
        categorias_medio_desempenho.append(categoria)
    else:
        performance = "Baixo"
        categorias_baixo_desempenho.append(categoria)

    print(f"{categoria:<15}: R$ {valor:,.2f} → Performance: {performance}")

# Relatório final com insights
print("\n📊 Relatório Resumido:")
print(f"• Categorias com **alto desempenho**  : {len(categorias_alto_desempenho)} → {categorias_alto_desempenho}")
print(f"• Categorias com **desempenho médio** : {len(categorias_medio_desempenho)} → {categorias_medio_desempenho}")
print(f"• Categorias com **baixo desempenho** : {len(categorias_baixo_desempenho)} → {categorias_baixo_desempenho}")

# Número total de categorias que bateram ou superaram a meta
categorias_acima_da_meta = [v for v in vendas_categorias.values() if v >= meta]
print(f"\n✅ Total de categorias acima da meta: {len(categorias_acima_da_meta)}")
