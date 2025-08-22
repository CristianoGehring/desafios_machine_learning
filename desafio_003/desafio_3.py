def estatisticas_basicas(dados):
    """
    Calcula estatísticas descritivas básicas
    Args: dados (list) - lista de valores numéricos
    Returns: dict - dicionário com estatísticas
    """
    if not dados:
        return None
    
    total = sum(dados)
    media = total / len(dados)
    dados_ordenados = sorted(dados)
    
    # Mediana
    n = len(dados_ordenados)
    if n % 2 == 0:
        mediana = (dados_ordenados[n//2-1] + dados_ordenados[n//2]) / 2
    else:
        mediana = dados_ordenados[n//2]
    
    # Máximo e mínimo
    maximo = max(dados)
    minimo = min(dados)
    
    return {
        'total': total,
        'media': media,
        'mediana': mediana,
        'maximo': maximo,
        'minimo': minimo,
        'amplitude': maximo - minimo
    }

def classificar_performance(valor, benchmarks):
    """
    Classifica performance baseada em benchmarks
    Args: 
        valor (float) - valor a ser classificado
        benchmarks (dict) - critérios de classificação
    Returns: str - classificação
    """
    if valor >= benchmarks['excelente']:
        return 'Excelente'
    elif valor >= benchmarks['bom']:
        return 'Bom'
    elif valor >= benchmarks['regular']:
        return 'Regular'
    else:
        return 'Baixo'
    
def gerar_relatorio_de_analise(trimestre:int, vendas:list, benchmarks:dict):
    """
    Imprime na tela o relatório de analise
    Returns: void
    """

    estatistica = estatisticas_basicas(vendas)

    classificacao = classificar_performance(estatistica['media'], benchmarks)
    
    print(f"- O trimestre {trimestre} teve uma média de R$ {estatistica['media']} entre as filiais, que foi clasificada como: {classificacao}")

vendas_q1 = [12500, 15800, 9200, 18900, 11400, 16700, 8900, 14300]
vendas_q2 = [14200, 17500, 10800, 19400, 13100, 18200, 9600, 15800]
vendas_q3 = [13800, 16200, 11500, 17800, 12900, 17100, 10200, 16400]

benchmarks = {
    'excelente': 17000,
    'bom': 14000,
    'regular': 11000
}

print(f"Levando em consideração o banchmark {benchmarks}")

for i,v in enumerate([vendas_q1, vendas_q2, vendas_q3]):
    gerar_relatorio_de_analise(i, v, benchmarks)