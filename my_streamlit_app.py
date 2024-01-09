import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Charger vos données
url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(url)

df_cars = df_cars.sort_values(by='year') 

# HEATMAP
selected_columns = ["mpg", "cylinders", "cubicinches", "hp", "weightlbs", "time-to-60", "year"]
subset_df = df_cars[selected_columns]

# Calcul matrice de corrélation
correlation_matrix = subset_df.corr()

# Streamlit app
st.title('Analyse des voitures')

# Filtrer par continent
st.sidebar.subheader('Filtrer par continent')
continent_filter = st.sidebar.selectbox('Choisir un continent', df_cars['continent'].unique())

# Filtrer les résultats par continent
filtered_df = df_cars[df_cars['continent'] == continent_filter]

# Afficher les données filtrées
st.subheader(f'Données pour le continent {continent_filter}')
st.write(filtered_df)

# Créer une disposition en ligne
st.subheader('Heatmap Matrice de Corrélation')
st.plotly_chart(px.imshow(correlation_matrix,
                           labels=dict(color='Correlation'),
                           x=selected_columns,
                           y=selected_columns,
                           title='Heatmap matrice corrélation'))

# ANIMATION
st.subheader('Animation Bar Chart')
st.plotly_chart(px.bar(df_cars, x="hp", y="cylinders", animation_frame="year",
                       range_x=[50, 180], range_y=[0, 20]))