import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Charger le dataset des voitures
url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(url)

# Ajouter une colonne pour la région en fonction de la colonne "origine"
df['Region'] = df['origin'].map({1: 'US', 2: 'Europe', 3: 'Japan'})

# Interface Streamlit
st.title("Analyse des voitures")

# Filtrer par région
region_filter = st.sidebar.selectbox("Filtrer par région", ['Toutes', 'US', 'Europe', 'Japan'])

if region_filter != 'Toutes':
    df_filtered = df[df['Region'] == region_filter]
else:
    df_filtered = df

# Afficher les données filtrées
st.write("Affichage des données pour la région :", region_filter)
st.write(df_filtered.head())

# Analyse de corrélation
st.header("Analyse de corrélation")

# Matrice de corrélation
corr_matrix = df_filtered.corr()
st.write("Matrice de corrélation :")
st.write(corr_matrix)

# Heatmap de corrélation
st.write("Heatmap de corrélation :")
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
st.pyplot()

# Distribution des caractéristiques
st.header("Distribution des caractéristiques")

# Sélectionner une caractéristique à afficher
feature_to_plot = st.sidebar.selectbox("Sélectionnez une caractéristique", df.columns)

# Distribution de la caractéristique sélectionnée
st.write(f"Distribution de {feature_to_plot} par région :")
sns.histplot(data=df_filtered, x=feature_to_plot, hue='Region', kde=True)
st.pyplot()