# 🚀 Desafio ML/AI Diário #3 - Dia 3/360
**⏱️ Tempo estimado:** 22 minutos
**📈 Nível:** Básico
**📅 Etapa:** Dia 3 de 360 - Fundamentos Python Avançado
**🎯 Conceitos:** Funções, parâmetros, análise estatística básica
**🧠 Foco:** Modularização de código e cálculos estatísticos
**🎓 Jornada:** 357 dias para especialista
**💻 Stack:** Python

## 📋 Descrição do Desafio
Baseado no seu progresso excepcional, vamos acelerar! Como Data Scientist, você precisa criar funções reutilizáveis para análise de dados de vendas. Você será responsável por construir um "mini toolkit" de análise que poderá ser usado em diferentes datasets - exatamente como bibliotecas profissionais fazem!

### 📝 Requisitos:
1. Criar uma função para calcular estatísticas básicas de uma lista de valores
2. Implementar uma função para classificar performance baseada em critérios
3. Desenvolver uma função para gerar relatório completo de análise
4. Testar todas as funções com dados de vendas trimestrais

### 📚 Conceitos que você vai aprender:
- **Funções:** Modularização essencial para códigos limpos em ML
- **Parâmetros e retorno:** Como criar APIs internas reutilizáveis
- **Estatística descritiva:** Média, mediana, desvio - base para feature engineering
- **DRY Principle:** Don't Repeat Yourself - fundamento da programação profissional

### 📊 Dados/Contexto:
Dados de vendas trimestrais de diferentes filiais:
```python
vendas_q1 = [12500, 15800, 9200, 18900, 11400, 16700, 8900, 14300]
vendas_q2 = [14200, 17500, 10800, 19400, 13100, 18200, 9600, 15800]
vendas_q3 = [13800, 16200, 11500, 17800, 12900, 17100, 10200, 16400]
```

### 💡 Exemplo passo a passo:
```python
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

# Teste suas funções com os dados fornecidos
```

### 🎯 Critérios de Avaliação:
- ✅ Funções bem estruturadas com docstrings
- 📊 Cálculos estatísticos corretos
- 💡 Uso eficiente de parâmetros e retornos
- 🧹 Código modular e reutilizável
- 📈 Análise comparativa entre trimestres

## 📚 Material de Apoio:
- [Python Functions - Documentação oficial](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Docstrings em Python](https://peps.python.org/pep-0257/)
- [Estatística descritiva básica](https://docs.python.org/3/library/statistics.html)

### 📈 Seu Progresso na Jornada:
**Dia 3 de 360 - Rumo à Especialização!**
- 🔥 Streak de desafios: 3 dias
- 📊 Progresso geral: 0.8% completo
- 🎯 Fase atual: Fundamentos Python Avançado
- 📅 Dias para especialista: 357
- 🧠 Habilidades desbloqueadas: Dicionários, loops, condicionais, list comprehensions
- 🏆 Marcos alcançados: **ACELERAÇÃO DETECTADA** - Progresso 2-3 dias à frente!

### 🎖️ Sistema de Progressão:
- 📘 **Iniciante** (Dias 1-120): Fundamentos sólidos ← **VOCÊ ESTÁ AQUI** (Acelerado!)
- 📗 **Intermediário** (Dias 121-240): ML e análise
- 📙 **Avançado** (Dias 241-300): Deep Learning e NLP  
- 📕 **Expert** (Dias 301-360): Projetos e especialização

### 🌟 **Nota especial - ACELERAÇÃO ATIVA:**
Devido ao seu desempenho excepcional nos Dias 1-2, este desafio já introduz conceitos que normalmente apareceriam no Dia 7-10! Você está se preparando mais rapidamente para trabalhar com bibliotecas como Pandas e NumPy.

**⭐ Desafio ativo! Continue neste ritmo e você será um especialista antes dos 360 dias!** 🎯