# Dashboard de Vendas de Carros e Recomendação via Mineração de Dados

## 📌 Sobre o Projeto
Este projeto consiste em um dashboard interativo para análise de vendas de veículos, desenvolvido utilizando **Streamlit**, **Pandas**, **Plotly Express** e **Scikit-learn**. Além da análise de vendas, o projeto implementa um modelo de **Árvore de Decisão** para recomendar veículos com base em características fornecidas pelo usuário.

## 👥 Integrantes do Grupo
- Bernardo Bomfim  
- Eduardo Braga  
- Lucas Pereira  

## 📊 Funcionalidades
- **Filtros Interativos**: Permitem a seleção de ano e fabricante para análise detalhada.
- **Métricas de Vendas**: Exibição de faturamento total, número de vendas, peso médio dos veículos e eficiência média de combustível.
- **Gráficos Dinâmicos**:
  - Faturamento por Data de Lançamento
  - Faturamento por Modelo
  - Participação de Mercado por Marca
  - Eficiência de Combustível por Modelo
- **Recomendação de Veículos**: Baseado no modelo de Árvore de Decisão, sugere um veículo ao usuário com base em marca, tipo e preço desejados.

## 🛠 Tecnologias Utilizadas
- **Python**
- **Streamlit**
- **Pandas**
- **Plotly Express**
- **Scikit-learn**

## 🚀 Como Rodar o Projeto
### 1️⃣ Clone o Repositório
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 2️⃣ Instale as Dependências
```bash
pip install streamlit pandas plotly scikit-learn
```

### 3️⃣ Execute o Dashboard
```bash
streamlit run dashboard.py
```

## 📂 Estrutura do Projeto
```
|-- Car_sales.csv
|-- README.md
|-- dashboard.py
|-- nova-formar-de-vender-veiculo.jpg.webp
```

## 📖 Explicação da Mineração de Dados
O modelo de recomendação utiliza uma **Árvore de Decisão** para prever qual veículo melhor se encaixa nas preferências do cliente. As etapas do modelo incluem:
1. **Codificação de Dados Categóricos**: Uso de `LabelEncoder` para transformar variáveis categóricas em numéricas.
2. **Normalização**: Aplicação de `StandardScaler` para padronizar os dados.
3. **Divisão do Dataset**: Separação dos dados em conjunto de treino (85%) e teste (15%).
4. **Treinamento**: Uso do `DecisionTreeClassifier` para criar o modelo preditivo.
5. **Predição**: O modelo retorna o carro mais adequado com base nas informações inseridas pelo usuário.

## 🔍 Conclusões
- Lançamentos de novos veículos impactam significativamente o faturamento.
- Algumas marcas dominam o mercado, influenciando estratégias de vendas.
- Eficiência de combustível é um critério importante para certos consumidores.
- A utilização de um modelo de **Árvore de Decisão** facilita a recomendação personalizada de veículos.

📌 **Esse projeto oferece uma análise detalhada do mercado automotivo e auxilia na tomada de decisões para consumidores e empresas!** 🚗📈

