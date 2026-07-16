import pandas as pd
import pickle as pkl
import streamlit as st
import numpy as np

df = pd.read_csv('Country-data.csv')
#print(df)

with open('Country-data.pkl', 'rb') as f:
    mdl = pkl.load(f)
print(type(mdl))

st.title("🌍 Country Development Analysis using K-Means Clustering")
st.image('Clustering_image.webp')
st.subheader("Group countries into Low-, Middle-, and High-income categories using socio-economic data.")

country = st.selectbox('Country',df['country'])
child_mort =st.number_input('Child Mortality',min_value=1.0,max_value=220.0,value=1.0)
exports = st.number_input('Exports',min_value=0.0,max_value=205.0,value=0.0)
health = st.number_input('Health',min_value=1.0,max_value=19.0,value=1.0)
imports = st.number_input('Imports',min_value=0.0,max_value=180.0,value=0.0)
income = st.number_input('Income',min_value=500,max_value=130000,value=500)
inflation = st.number_input('Inflation',min_value=-10.0,max_value=110.0,value=1.0)
life_expec = st.number_input('Life-Expectancy',min_value=30.0,max_value=85.0,value=30.0)
total_fer = st.number_input('Total Fertility',min_value=1.0,max_value=9.0,value=1.0)
gdpp = st.number_input('GDPP',min_value=200.0,max_value=110000.0,value=200.0)


x_values= pd.DataFrame({
    'child_mort':[child_mort],'exports':[exports],'health':[health],
    'imports':[imports],'income':[income],'inflation':[inflation],'life_expec':[life_expec],
    'total_fer':[total_fer],'gdpp':[gdpp]
})

st.header('Input Submitted for Processing')
st.table(x_values)

if st.button('Predict'):
    prediction = mdl.predict(x_values)
    if prediction == 'High-income':
        st.success('More Developed Country')
    elif prediction == 'Middle-income':
        st.success('Less Developed Country')
    else:
        st.error('Poor Country')


def footer():
    st.write("---")
    st.write("Heart Disease Prediction System")
    st.write("Developed by MEHRAN KHAN")
    st.write("© 2026 All Rights Reserved")
footer()

st.markdown("""
<style>

.stApp{
background:
linear-gradient(rgba(15,23,42,.70),rgba(15,23,42,.70)),
url("https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?auto=format&fit=crop&w=1920&q=80");

background-size:cover;
background-position:center;
background-attachment:fixed;
}

.block-container{
background:rgba(255,255,255,.80);
padding:35px;
border-radius:22px;
box-shadow:0 15px 40px rgba(0,0,0,.35);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* White Predict Button */
div.stButton > button {
    background: white !important;
    color: black !important;
    border: 2px solid black !important;
    border-radius: 12px !important;
    font-weight: bold !important;
}

div.stButton > button:hover {
    background: #f2f2f2 !important;
    color: black !important;
    border: 2px solid black !important;
}

div.stButton > button:focus {
    background: white !important;
    color: black !important;
    border: 2px solid black !important;
    box-shadow: none !important;
}

</style>
""", unsafe_allow_html=True)




