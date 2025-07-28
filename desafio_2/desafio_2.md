# 🚀 Desafio ML/AI Diário #2 - Dia 2/360
**⏱️ Tempo estimado:** 18 minutos
**📈 Nível:** Iniciante
**📅 Etapa:** Dia 2 de 360 - Fundamentos Python
**🎯 Conceitos:** Loops, condicionais, listas, análise de padrões
**🧠 Foco:** Estruturas de controle para análise de dados
**🎓 Jornada:** 358 dias para especialista
**💻 Stack:** Python

## 📋 Descrição do Desafio
Baseado na sua excelente performance no Dia 1, vamos acelerar um pouco! Como analista de dados, você precisa analisar o desempenho de vendas por categoria de produtos e identificar padrões. Este tipo de análise é fundamental para algoritmos de recomendação e segmentação de clientes.

### 📝 Requisitos:
1. Analisar vendas de diferentes categorias de produtos
2. Classificar o desempenho de cada categoria (Alto/Médio/Baixo)
3. Identificar quantas categorias estão acima da meta
4. Criar um relatório resumido com insights

### 📚 Conceitos que você vai aprender:
- **Loops (for):** Iteração sobre dados - base para processamento de datasets
- **Condicionais (if/elif/else):** Lógica de decisão usada em feature engineering
- **Listas:** Estrutura fundamental para arrays em NumPy e Pandas
- **Análise de padrões:** Pensamento analítico essencial para ML

### 📊 Dados/Contexto:
Você tem dados de vendas por categoria da sua empresa:
```python
vendas_categorias = {
    "Eletrônicos": 15750.80,
    "Roupas": 8920.45,
    "Casa e Jardim": 12300.60,
    "Esportes": 6780.30,
    "Livros": 4560.90,
    "Alimentação": 18900.75,
    "Beleza": 9840.20
}
```

**Meta mensal por categoria:** R$ 10.000

### 💡 Exemplo passo a passo:
```python
# Passo 1: Definir critérios de classificação
meta = 10000
categorias_alto_desempenho = []
categorias_baixo_desempenho = []

# Passo 2: Analisar cada categoria
for categoria, valor in vendas_categorias.items():
    if valor >= meta * 1.2:  # 20% acima da meta
        performance = "Alto"
        categorias_alto_desempenho.append(categoria)
    elif valor >= meta:  # Entre meta e 20% acima
        performance = "Médio"
    else:  # Abaixo da meta
        performance = "Baixo"
        categorias_baixo_desempenho.append(categoria)
    
    print(f"{categoria}: R$ {valor:,.2f} - Performance: {performance}")

# Passo 3: Gerar insights
print(f"\nCategorias acima da meta: {len([v for v in vendas_categorias.values() if v >= meta])}")
```

### 🎯 Critérios de Avaliação:
- ✅ Uso correto de loops e condicionais
- 📊 Classificação precisa das categorias
- 💡 Geração de insights relevantes
- 🧹 Código organizado e legível

## 📚 Material de Apoio:
- [Python - Estruturas de controle](https://docs.python.org/3/tutorial/controlflow.html)
- [Loops em Python](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Condicionais if/elif/else](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

### 📈 Seu Progresso na Jornada:
**Dia 2 de 360 - Rumo à Especialização!**
- 🔥 Streak de desafios: 2 dias
- 📊 Progresso geral: 0.6% completo
- 🎯 Fase atual: Fundamentos Python
- 📅 Dias para especialista: 358
- 🧠 Habilidades desbloqueadas: Dicionários, estruturas de controle
- 🏆 Marcos alcançados: Soluções acima da média no Dia 1!

### 🎖️ Sistema de Progressão:
- 📘 **Iniciante** (Dias 1-120): Fundamentos sólidos ← **VOCÊ ESTÁ AQUI**
- 📗 **Intermediário** (Dias 121-240): ML e análise
- 📙 **Avançado** (Dias 241-300): Deep Learning e NLP  
- 📕 **Expert** (Dias 301-360): Projetos e especialização

### 🌟 **Nota especial:**
Seu desempenho no Dia 1 foi excepcional! Por isso, este desafio já incorpora conceitos que você claramente domina. Continue assim que logo estaremos trabalhando com bibliotecas de Data Science!

**⭐ Desafio ativo! Cada dia te aproxima da especialização!** 🎯