import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.title("Análisis Titanic")
st.markdown("*Mónica Ibarra Herrera*")
st.image('titanic_imagen.jpg')
st.header("Data Set")

df = pd.read_csv("Titanic-Dataset.csv") 
df.columns=["passenger_id","survived","class","name","sex","age","sib_spouses","parents_children","ticket","fare","cabin","port"] 
st.dataframe(df)
print('\n')

st.header("Histograma sobrevivientes")
survived_agrupado = df.groupby("survived")
fig, ax = plt.subplots(figsize=(6,4))
for i, survived_agrupado in survived_agrupado:
    ax.hist(survived_agrupado["survived"], alpha = 0.5, bins=2, label=str(i))
ax.set_title('Sobrevivientes', fontname= 'Times New Roman', fontsize= 15)
ax.set_xlabel('0 No sobrevivieron, 1 Sobrevivieron', fontname= 'Times New Roman', fontsize=12)
ax.legend()
st.pyplot(fig)
st.markdown("*Hallazgo del histograma*")
st.markdown("Como podemos ver la mayoría de los pasajeros no sobrevivió, más de 500 murieron.")

st.header("Histograma clases")
clases_agrupado = df.groupby("class")
fig, ax = plt.subplots(figsize=(6,4))
for x, clases_agrupado in clases_agrupado:
    ax.hist(clases_agrupado["class"], alpha = 0.5, bins=3, label=str(x))
ax.set_title('# de Clase ', fontname= 'Times New Roman', fontsize= 15)
ax.set_xlabel('Clases', fontname= 'Times New Roman', fontsize=12)
ax.legend()
st.pyplot(fig)
st.markdown("*Hallazgo del histograma*")
st.markdown("Como podemos visualizar en el histograma la clase en la que más pasajeros viajaban es en la tercera con aproximadamente 500 pasajeros")

st.header("Histograma género")
fig, ax = plt.subplots(figsize=(6,4))
colors = {'male': 'blue', 'female': 'red'}
for gender, data in df.groupby('sex'):
    ax.hist(data['sex'], alpha=0.5, bins=2, color=colors[gender], label=gender)
ax.set_title('Género de los pasajeros', fontname='Times New Roman', fontsize=15)
ax.set_xlabel('Género', fontname='Times New Roman', fontsize=12)
ax.legend()
st.pyplot(fig)
st.markdown("*Hallazgo del histograma*")
st.markdown("Se puede visualizar que había más pasajeros hombres que mujeres, con aproximadamente 570 hombres y aproximadamente 310 mujeres")

st.header("Histograma edad")
fig, ax = plt.subplots(figsize=(6,4))
bins = range(0, 101, 10)
ax.hist(df["age"], alpha=0.5, bins=bins,color = 'lightblue', edgecolor='black')
ax.set_title('Edades', fontname='Times New Roman', fontsize=15)
ax.set_xlabel('Edades', fontname='Times New Roman', fontsize=12)
st.pyplot(fig)
st.markdown("*Hallazgo del histograma*")
st.markdown("Como podemos ver en la gráfica la edad más frecuente es entre 20 y 30 años, con más de 200 pasajeros")

st.header("Histograma de # de hermanos o esposos a bordo")
sibsp_agrupado = df.groupby("sib_spouses")
fig, ax = plt.subplots(figsize=(6,4))
for w, sibsp_agrupado in sibsp_agrupado:
    ax.hist(sibsp_agrupado["sib_spouses"], alpha = 0.5, bins=2, label=str(w))
ax.set_title('# de hermanos o esposos a bordo', fontname= 'Times New Roman', fontsize= 15)
ax.set_xlabel('# de hermanos o esposos', fontname= 'Times New Roman', fontsize=12)
ax.legend()
st.pyplot(fig)
st.markdown("*Hallazgo del histograma*")
st.markdown("En el histograma se puede ver que casi no habían hermanos o esposo a bordo, 600 pasajeros no llevaban ni hermanos ni pareja")

st.header("Histograma de # de padres o hijos a bordo")
sibsp_agrupado = df.groupby("parents_children")
fig, ax = plt.subplots(figsize=(6,4))
for w, sibsp_agrupado in sibsp_agrupado:
    ax.hist(sibsp_agrupado["parents_children"], alpha = 0.5, bins=2, label=str(w))
ax.set_title('# de padres u hijos a bordo', fontname= 'Times New Roman', fontsize= 15)
ax.set_xlabel('# de padres u hijos', fontname= 'Times New Roman', fontsize=12)
ax.legend()
st.pyplot(fig)
st.markdown("*Hallazgo del histograma*")
st.markdown("Se puede visualizar que la mayoría de los pasajeros, aproximadamente 670 pasajeros no viajan ni padres o hijos")

st.header("Histograma de tarifa del boleto")
fig, ax = plt.subplots(figsize=(6,4))
bins = range(0, 520, 15)
ax.hist(df["fare"], alpha=0.5, bins=bins,color = 'pink', edgecolor='black')
ax.set_title('Tarifa boleto', fontname='Times New Roman', fontsize=15)
ax.set_xlabel('Tarifa', fontname='Times New Roman', fontsize=12)
st.pyplot(fig)
st.markdown("*Hallazgo del histograma*")
st.markdown("En el histograma se puede ver que la tarifa de la mayoría está aproximadamente entre 0 y 25 euros ya que la mayor clase que abordó fue la tercera de la tarifa con más de 400 pasajeros")

st.header("Histograma de puertos")
puertos_agrupado = df.groupby("port")
fig, ax = plt.subplots(figsize=(6,4))
for u, puertos_agrupado in puertos_agrupado:
    ax.hist(puertos_agrupado["port"], alpha = 0.5, bins=2, label=str(u))
ax.set_title('Puertos de abordaje', fontname= 'Times New Roman', fontsize= 15)
ax.set_xlabel('Puertos', fontname= 'Times New Roman', fontsize=12)
ax.legend()
st.pyplot(fig)
st.markdown("*Hallazgo del histograma*")
st.markdown("El histograma muestra que el puerto donde abordaron más pasajeros fue en el S, después en el C y después en el Q")