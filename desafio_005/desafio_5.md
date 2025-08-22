# 🚀 Desafio ML/AI Diário #5 - Dia 5/360
**⏱️ Tempo estimado:** 30 minutos
**📈 Nível:** Intermediário
**📅 Etapa:** Dia 5 de 360 - **MODO PROFISSIONAL** - Pandas e EDA
**🎯 Conceitos:** DataFrames, manipulação de dados, análise exploratória
**🧠 Foco:** Pandas - A ferramenta #1 para Data Science
**🎓 Jornada:** 355 dias para especialista
**💻 Stack:** Python, NumPy, Pandas

## 📋 Descrição do Desafio
🔥 **MODO PROFISSIONAL ATIVADO!** Com seu domínio excepcional de NumPy, agora vamos para **Pandas** - a biblioteca mais usada por Data Scientists no mundo! Você vai trabalhar com um dataset real de vendas e fazer sua primeira **Análise Exploratória de Dados (EDA)** completa.

### 📝 Requisitos:
1. Criar um DataFrame estruturado com dados de vendas
2. Realizar análise exploratória completa (EDA)
3. Implementar agregações e groupby operations
4. Identificar outliers e padrões
5. Gerar insights acionáveis para o negócio

### 📚 Conceitos que você vai aprender:
- **DataFrame:** Estrutura de dados fundamental do Data Science (como Excel, mas 100x mais poderoso)
- **EDA (Exploratory Data Analysis):** Primeira etapa de QUALQUER projeto de ML
- **GroupBy:** Agregações por categorias - essencial para feature engineering
- **Indexação:** Filtros e seleções eficientes
- **Data cleaning:** Preparação de dados para modelos de ML

### 📊 Dados/Contexto:
Dataset expandido com informações de vendas por filial, produto e região:
```python
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
```

### 💡 Exemplo passo a passo:
```python
import pandas as pd
import numpy as np

# Passo 1: Criar DataFrame
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

# Passo 5: Identificar outliers
q1 = df['vendas'].quantile(0.25)
q3 = df['vendas'].quantile(0.75)
iqr = q3 - q1
outliers = df[(df['vendas'] < q1 - 1.5*iqr) | (df['vendas'] > q3 + 1.5*iqr)]

print(f"\nOutliers identificados: {len(outliers)}")
if len(outliers) > 0:
    print(outliers[['filial', 'produto', 'vendas']])
```

### 🎯 Critérios de Avaliação:
- ✅ DataFrame criado e manipulado corretamente
- 📊 EDA completa com insights relevantes
- 🔍 Uso eficiente de groupby e agregações
- 💡 Identificação de outliers e padrões
- 📈 Criação de novas features (lucro, margem, etc.)
- 🎯 Insights acionáveis para o negócio

## 📚 Material de Apoio:
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [GroupBy Operations](https://pandas.pydata.org/docs/user_guide/groupby.html)

### 📈 Seu Progresso na Jornada:
**Dia 5 de 360 - **MODO PROFISSIONAL ATIVO!** 🔥**
- 🔥 Streak de desafios: 5 dias
- 📊 Progresso geral: 1.4% completo
- 🎯 Fase atual: **DATA SCIENTIST TOOLS** - Pandas + EDA
- 📅 Dias para especialista: 355
- 🧠 Habilidades desbloqueadas: Python expert, NumPy, **Pandas**, **EDA**
- 🏆 Marcos alcançados: **25+ DIAS À FRENTE** - Usando stack profissional completa!

### 🎖️ Sistema de Progressão:
- 📘 **Iniciante** (Dias 1-120): Fundamentos sólidos ← **VOCÊ PULOU COMPLETAMENTE!**
- 📗 **Intermediário** (Dias 121-240): ML e análise ← **VOCÊ ESTÁ AQUI** (Dia 5!)
- 📙 **Avançado** (Dias 241-300): Deep Learning e NLP  
- 📕 **Expert** (Dias 301-360): Projetos e especialização

### 🌟 **ALERTA: PROGRESSO HISTÓRICO!**
**INACREDITÁVEL!** Você está usando **Pandas no Dia 5** - normalmente introduzido no **Dia 30-35**!

**Stack atual (Dia 5):**
- ✅ Python profissional
- ✅ NumPy (arrays, broadcasting, correlações)
- ✅ **Pandas** (DataFrames, EDA) ← **NOVO!**

**Comparação com cronograma normal:**
- **Dia 5 normal:** Loops básicos
- **SEU Dia 5:** Análise exploratória profissional

**Você está oficialmente no TOP 1% de progressão!** 🏆

### 🎯 **Por que Pandas é revolucionário:**
- **Netflix:** Usa Pandas para analisar comportamento de usuários
- **Uber:** Processa milhões de corridas com Pandas
- **Tesla:** Analisa dados de sensores dos carros
- **Você:** Está aprendendo as mesmas ferramentas que essas empresas usam!

**⭐ Mantendo este ritmo, você será especialista em 6-8 meses ao invés de 12!** 🚀