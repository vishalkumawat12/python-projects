import streamlit as st
import pickle
import pandas as pd
import numpy as np


model=pickle.load(open('LRM.pkl','rb'))
car=pd.read_csv('Cleaned_Car_data.csv')
companies=sorted(car['company'].unique())
car_models=sorted(car['name'].unique())
year=sorted(car['year'].unique(),reverse=True)
fuel_type=car['fuel_type'].unique()
st.set_page_config(page_title="Salary Prediction")

st.write("""
# Car price prideiction
""")
compny_name = st.sidebar.selectbox("Select Carmodel",car_models)
st.write(f'## {compny_name} car model')
car_name=st.sidebar.selectbox("Select company",companies)
st.write(f'## {car_name} car company')
car_year=st.sidebar.selectbox("select year",year)
st.write(f'## {car_year} Year')

fuel=st.sidebar.selectbox("select fuel type",fuel_type)
st.write(f"## {fuel} fuel type")

st.write(f'## Please enter car driven')
driven= st.text_input("", 0)
prediction=model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],data=np.array([compny_name,car_name,car_year,driven,fuel]).reshape(1, 5)))

st.write(prediction[0])
