import streamlit as st
import numpy as np
import pickle
import pandas as pd

st.set_page_config(page_title="flawer name Prediction")

st.write("""
# flawer name prediction
""")
model=pickle.load(open('fla.pkl','rb'))


st.write(f'## Please Enter Sepal length of flawer')
chSeplen= st.text_input("size must in bitwin 4.3 to 7.9 for best result...", 0)

st.write(f'## Please Enter Sepal width of flawer')
chsepwid= st.text_input("size must in bitwin 2.0 to 4.4 for best result...", 0)


st.write(f'## Please Enter petal length of flawer')
chpetlen= st.text_input("size must in bitwin 1.0 to 6.9 for best result...", 0)


st.write(f'## Please Enter petal width of flawer')
chpetwid= st.text_input("size must in bitwin 0.1 to 2.5 for best result...", 0)

prediction=model.predict(pd.DataFrame(columns=['SepalLengthCm','SepalWidthCm','SepalWidthCm','PetalWidthCm'],data=np.array([chSeplen,chsepwid,chpetlen,chpetwid]).reshape(1,4)))
st.write(f" # {prediction[0]}")
