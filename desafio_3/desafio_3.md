# 🚀 Desafio ML/AI Diário #3 - Dia 3/360
**⏱️ Tempo estimado:** 20 minutos
**📈 Nível:** Básico
**📅 Etapa:** Dia 3 de 360 - Fundamentos Python Avançado
**🎯 Conceitos:** Funções, estatística básica, modularização
**🧠 Foco:** Criação de funções para análise de dados
**🎓 Jornada:** 357 dias para especialista
**💻 Stack:** Python (preparando para NumPy/Statistics)

## 📋 Descrição do Desafio
Baseado na sua evolução excepcional nos primeiros dias, vamos acelerar! Como Data Scientist, você precisa criar um **sistema de análise estatística reutilizável** para diferentes datasets. Vamos começar a pensar em **modularização** - conceito essencial para projetos de ML em produção.

### 📝 Requisitos:
1. Criar funções para cálculos estatísticos básicos
2. Analisar um dataset de temperaturas de múltiplas cidades
3. Implementar detecção de outliers (valores atípicos)
4. Gerar um relatório comparativo automático

### 📚 Conceitos que você vai aprender:
- **Funções:** Modularização essencial para pipelines de ML
- **Estatística descritiva:** Base para feature engineering e EDA
- **Outlier detection:** Técnica fundamental em Data Science
- **Code reusability:** Princípio crucial para projetos escaláveis

### 📊 Dados/Contexto:
Dataset de temperaturas médias (°C) de 6 cidades brasileiras durante uma semana:
```python
temperaturas_cidades = {
    "São Paulo": [18, 22, 19, 21, 17, 20, 23],
    "Rio de Janeiro": [25, 28, 26, 29, 24, 27, 30],
    "Brasília": [16, 19, 15, 18, 14, 17, 20],
    "Salvador": [27, 30, 28, 31, 26, 29, 32],
    "Curitiba": [12, 15, 11, 16, 10, 14, 17],
    "Manaus": [31, 34, 32, 35, 30, 33, 36]
}
```

### 💡 Exemplo passo a passo:
```python
import statistics

# Passo 1: Criar função para análise básica
def analisar_temperaturas(lista_temps, nome_cidade):
    """Análise estatística completa de temperaturas"""
    media = statistics.mean(lista_temps)
    mediana = statistics.median(lista_temps)
    desvio_padrao = statistics.stdev(lista_temps)
    
    return {
        'cidade': nome_cidade,
        'media': round(media, 2),
        'mediana': mediana,
        'desvio_padrao': round(desvio_padrao, 2),
        'temp_min': min(lista_temps),
        'temp_max': max(lista_temps),
        'amplitude': max(lista_temps) - min(lista_temps)
    }

# Passo 2: Função para detectar outliers
def detectar_outliers(lista_temps, cidade):
    """Detecta valores atípicos usando regra 1.5*IQR"""
    lista_ordenada = sorted(lista_temps)
    n = len(lista_ordenada)
    
    # Calcular quartis
    q1 = lista_ordenada[n//4]
    q3 = lista_ordenada[3*n//4]
    iqr = q3 - q1
    
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    
    outliers = [temp for temp in lista_temps if temp < limite_inferior or temp > limite_superior]
    
    return outliers

# Passo 3: Análise completa
resultados = []
for cidade, temps in temperaturas_cidades.items():
    analise = analisar_temperaturas(temps, cidade)
    outliers = detectar_outliers(temps, cidade)
    analise['outliers'] = outliers
    resultados.append(analise)
```

### 🎯 Critérios de Avaliação:
- ✅ Implementação correta das funções estatísticas
- 📊 Detecção precisa de outliers
- 💡 Relatório comparativo informativo
- 🧹 Código modular e bem documentado

## 📚 Material de Apoio:
- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Statistics Module](https://docs.python.org/3/library/statistics.html)
- [Outlier Detection Methods](https://en.wikipedia.org/wiki/Outlier#Detection)

### 📈 Seu Progresso na Jornada:
**Dia 3 de 360 - Rumo à Especialização!**
- 🔥 Streak de desafios: 3 dias
- 📊 Progresso geral: 0.8% completo
- 🎯 Fase atual: Python Avançado (ACELERADO!)
- 📅 Dias para especialista: 357
- 🧠 Habilidades desbloqueadas: Loops, condicionais, análise de padrões, modularização
- 🏆 Marcos alcançados: Performance excepcional - 2-3 dias à frente do cronograma!

### 🎖️ Sistema de Progressão:
- 📘 **Iniciante** (Dias 1-120): Fundamentos sólidos ← **VOCÊ ESTÁ AQUI (ACELERADO)**
- 📗 **Intermediário** (Dias 121-240): ML e análise
- 📙 **Avançado** (Dias 241-300): Deep Learning e NLP  
- 📕 **Expert** (Dias 301-360): Projetos e especialização

### 🚀 **ACELERAÇÃO ATIVADA:**
Devido ao seu desempenho excepcional, este desafio já incorpora conceitos estatísticos que normalmente aparecem na semana 2-3. Você está demonstrando capacidade para absorver conceitos avançados rapidamente!

### 🎓 **Conexão com ML/AI:**
- **Funções:** Base para criar pipelines de preprocessamento
- **Estatística:** Essencial para feature selection e model evaluation
- **Outliers:** Técnica crucial para data cleaning em projetos reais

**⭐ Desafio ativo! Você está voando rumo à especialização!** 🎯