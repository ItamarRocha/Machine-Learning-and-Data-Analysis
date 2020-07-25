import pandas as pd
import numpy as np
import streamlit as st

@st.cache #doenst reload the data every F5
def data(filename, columns):
    df = pd.read_csv(filename)
    df = df[columns]
    df = df.loc[(df.price < df.price.mean() + df.price.std()) & (df.price > 5)]
    return df

df = data("listings.csv", ["latitude","longitude","price"])

st.title("Airbnb London price distribution") # show title
st.markdown(f"""
    Dashboard to analyse the price distribution of Airbnb London

    Loading {df.shape[0]} input lines.
""") # markdown


st.sidebar.header("Configurations") #sidebar

# Dataframe
if st.sidebar.checkbox("Show Dataframe"):
    st.write(df)

# map plot
st.subheader("Map")
selected_input = st.empty()
st.sidebar.subheader("Price")
price = st.sidebar.slider("select how much you can pay for", df.price.min(), df.price.max(), 300)
df_filtered = df[(df.price >= price - 10) & (df.price <= price + 10)]
selected_input.text(df_filtered.shape[0])
st.map(df_filtered)

st.subheader("Histogram")
hist = np.histogram(df.price, bins = 10, range=(0,10))[0]
st.bar_chart(hist)

