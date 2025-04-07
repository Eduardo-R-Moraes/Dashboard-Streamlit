import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler

st.set_page_config(layout="wide")

df = pd.read_csv("car_sales.csv", sep=",", decimal=".")
df["Latest_Launch"] = pd.to_datetime(df["Latest_Launch"])
df = df.sort_values("Latest_Launch")

df["Ano"] = df["Latest_Launch"].dt.year
year = st.sidebar.selectbox("Ano", df["Ano"].unique())
df_filtered = df[df["Ano"] == year]

marcas = st.sidebar.multiselect("Marca", df["Manufacturer"].unique(), default=df["Manufacturer"].unique())
st.sidebar.image("nova-formar-de-vender-veiculo.jpg.webp", use_container_width=True)

if marcas:
    df_filtered = df_filtered[df_filtered["Manufacturer"].isin(marcas)]

st.title("Dashboard de Vendas de Carros")
st.write("Business Intelligence")

st.markdown("## Resumo")
total_faturamento = df_filtered["Price_in_thousands"].sum() * 1000
total_vendas = df_filtered.shape[0]
media_eficiencia = df_filtered["Fuel_efficiency"].mean()
media_peso = df_filtered["Curb_weight"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Faturamento", value=f"R${total_faturamento:.2f}".replace(".", ","))

with col2:
    st.metric(label="Total Vendas", value=total_vendas)

with col3:
    st.metric(label="Peso Medio (kg)", value=f"{media_peso:.3f}")

with col4:
    st.metric(label="Eficiência Média (Mpl)", value=f"{media_eficiencia:.2f}".replace(".", ","))

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

fig_date = px.bar(df_filtered, x="Latest_Launch", y="Price_in_thousands", color="Vehicle_type", title="Faturamento por Data de Lançamento")
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(df_filtered, x="Latest_Launch", y="Model", color="Vehicle_type", title="Faturamento por Modelo", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

fig_kind = px.pie(df_filtered, values="Price_in_thousands", names="Manufacturer", title="Faturamento por Marca de Veículo")
col3.plotly_chart(fig_kind, use_container_width=True)

fuel_efficiency = df_filtered.groupby("Model")["Fuel_efficiency"].mean().reset_index()
fig_rating = px.bar(fuel_efficiency, x="Model", y="Fuel_efficiency", title="Eficiência Média por Modelo")
col4.plotly_chart(fig_rating, use_container_width=True)

st.markdown("## Recomendação de Carros para um Cliente")

X = df[["Manufacturer", "Vehicle_type", "Price_in_thousands"]]
y = df["Model"]

le_marca = LabelEncoder()
le_tipo = LabelEncoder()
le_modelo = LabelEncoder()

X["Manufacturer"] = le_marca.fit_transform(X["Manufacturer"])
X["Vehicle_type"] = le_tipo.fit_transform(X["Vehicle_type"])
y_encoded = le_modelo.fit_transform(y)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.15, random_state=0)

dt = DecisionTreeClassifier(random_state=0)
dt.fit(X_train, y_train)

st.markdown("### Insira os detalhes do cliente para receber uma recomendação de carro")
marca_input = st.selectbox("Marca", df["Manufacturer"].unique())
tipo_input = st.selectbox("Tipo de Veículo", df["Vehicle_type"].unique())
preco_input = st.number_input("Preço (em milhares)", min_value=0.0, step=0.01)

novo_cliente = pd.DataFrame([[le_marca.transform([marca_input])[0], le_tipo.transform([tipo_input])[0], preco_input]],
                            columns=["Manufacturer", "Vehicle_type", "Price_in_thousands"])

novo_cliente_scaled = scaler.transform(novo_cliente)
predicao = dt.predict(novo_cliente_scaled)
carro_recomendado = le_modelo.inverse_transform(predicao)

st.markdown("### Carro recomendado para o cliente")
st.success(f"Carro recomendado: {carro_recomendado[0]}")
