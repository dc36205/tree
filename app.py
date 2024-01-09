# Section-1 Loading libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Section-2 Loading the data        
df = pd.read_csv('vehicles_us.csv') 
#df_car_data = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/datasets/vehicles_us.csv') 

st.title('Sales car project')
st.write(("A summary information"))

# Some sort of cleaning task over the dataset
#df = df.dropna(subset="model_year")
#df_car_data = df.dropna(subset = "cylinders")
#df_car_data = df.dropna(subset = "odometer")
#df_car_data = df.dropna(subset = "paint_color")

df[df['model_year'].isna() == True].count()
df.drop(['is_4wd', 'paint_color'] , axis=1)
'''
The dataset Sales Car contains information about features of an amount of cars,
that ascending up to 51524 cars. In a simple project some key features 
are shown through graphs like histogram and scatter plot.
'''
# Section-4 Functionalities

#selected_x_var = st.selectbox('What do want the x variable to be?',  ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']) 

#hist_button = st.button('Building histogram')        

def histogram():
    st.write('Histogram')                 
    fig = px.histogra(df, x="price")        
    st.plotly_chart(fig, use_container_width=True)


#if hist_button: 
            #st.write('Histogram')                 
            #fig = px.histogra, x="price")        
            #st.plotly_chart(fig, use_container_width=True)             


def scatter():
            st.write('Scatter type vs price')
            fig = px.scatter(df, x="type", y="price")         
            st.plotly_chart(fig, use_container_width=True) 

#build_histogram = st.checkbox('Building scatter')

#if build_histogram: 
            #st.write('Scatter type vs price')
            #fig = px.scatter(df, x="type", y="price")         
            #st.plotly_chart(fig, use_container_width=True) 

st.sidebar.header('Settings')

actions = {'Histogram': histogram, 'Plot': scatter}
choices = st.sidebar.multiselect('Choose task:', ['Histogram', 'Plot'])
for choice in choices:
    result = actions[choice]()