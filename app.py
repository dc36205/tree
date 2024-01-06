import pandas as pd
import plotly.express as px
import streamlit as st
#import time
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

#progress_bar = st.sidebar.progress(0)
#status_text = st.sidebar.empty()

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True) 
            time.sleep(0.05)

#progress_bar.empty()

#import streamlit as st

# crear una casilla de verificación para el scatter
build_histogram = st.checkbox('Construir un scatter')

if build_histogram: # si la casilla de verificación está seleccionada
            st.write('Construir un scatter para la columna odómetro')
            # crear un scatter
            fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True) 


