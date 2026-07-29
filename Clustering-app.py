import pandas as pd
import pickle as pkl
import streamlit as st
import numpy as np
import sqlite3


df = pd.read_csv('Country-data.csv')
#print(df)

with open('Country-data.pkl', 'rb') as f:
    mdl = pkl.load(f)
print(type(mdl))

#Create a database
conn = sqlite3.connect('Country-database.csv')
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Country_table(ID INTEGER PRIMARY KEY AUTOINCREMENT,
COUNTRY TEXT,CHILD_MORT REAL,EXPORTS REAL,HEALTH REAL , IMPORTS REAL,INCOME INTEGER,INFLATION REAL,
LIFE_EXPECTANCY REAL,TOTAL_FERTILITY REAL,GDPP REAL,PREDICTION TEXT)""")
conn.commit()


#Streamlit code
st.title("🌍 Country Development Analysis using K-Means Clustering")
st.image('Clustering_image.webp')
st.subheader("Group countries into Low-, Middle-, and High-income categories using socio-economic data.")
country = st.selectbox('Country',df['country'])
child_mort =st.number_input("Child Mortality Rate (Range: 1.0–220.0)",min_value=1.0,max_value=220.0,value=1.0)
exports = st.number_input("Exports (Range: 0.0–205.0)",min_value=0.0,max_value=205.0,value=0.0)
imports = st.number_input("Imports (% of GDP) (Range: 0.0–180.0)",min_value=0.0,max_value=180.0,value=0.0)
income = st.number_input("Annual Income per Person (US$) (Range: 500–130000)",min_value=500,max_value=130000,value=500)
inflation = st.number_input("Inflation Rate (%) (Range: -10.0–110.0)",min_value=-10.0,max_value=110.0,value=1.0)
health = st.slider("Health Expenditure (%)(Range: 1.0–19.0)",min_value=1.0,max_value=19.0,value=1.0)
life_expec = st.slider("Life Expectancy (Years) (Range: 30.0–85.0)",min_value=30.0,max_value=85.0,value=30.0)
total_fer = st.slider("Total Fertility Rate (Range: 1.0–9.0)",min_value=1.0,max_value=9.0,value=1.0)
gdpp = st.number_input("GDP per Capita (US$) (Valid Range: 200–110000)",min_value=200.0,max_value=110000.0,value=200.0)


x_values= pd.DataFrame({
    'child_mort':[child_mort],'exports':[exports],'health':[health],
    'imports':[imports],'income':[income],'inflation':[inflation],'life_expec':[life_expec],
    'total_fer':[total_fer],'gdpp':[gdpp]
})

st.header('Input Submitted for Processing')
st.table(x_values)

#Prediction button
if st.button('Predict'):
    prediction = mdl.predict(x_values)
    if prediction == 'High-income':
        Result = 'HIGH'
        st.success('More Developed Country')
    elif prediction == 'Middle-income':
        Result = 'MEDIUM'
        st.success('Less Developed Country')
    else:
        Result = 'LOW'
        st.error('Poor Country')
    cursor.execute("""INSERT INTO Country_table(COUNTRY,CHILD_MORT,EXPORTS,HEALTH , IMPORTS,INCOME ,INFLATION,
    LIFE_EXPECTANCY,TOTAL_FERTILITY,GDPP,PREDICTION)VALUES(?,?,?,?,?,?,?,?,?,?,?)""",(country,
    child_mort,exports,health,imports,income,inflation,life_expec,total_fer,gdpp,prediction))
    conn.commit()
    st.success('Saved Successfully')

#Admin Section
if st.checkbox('Prediction Records'):
    password = st.text_input('Enter Password',type = 'password')
    if password == '1234':
        st.success('Welcome')
        data = pd.read_sql_query('SELECT * FROM Country_table',conn)
        st.dataframe(data,hide_index=True)
        st.header('Update Record')

        id_record = st.number_input("Select Record ID",min_value=1)
        column = st.selectbox('Select Column',['COUNTRY','CHILD_MORT','EXPORTS','HEALTH' ,
        'IMPORTS','INCOME' ,'INFLATION','LIFE_EXPECTANCY','TOTAL_FERTILITY','GDPP','PREDICTION'])
        if column == 'PREDICTION':
            val = st.selectbox('value',['HIGH','MEDIUM','LOW'])
        else:
            val = st.text_input('New Value')
        if st.button('Update'):
            cursor.execute(f"UPDATE Country_table SET {column}=? WHERE ID =?",(val,id_record))
            conn.commit()
            st.success('Updated Successfully')



def footer():
    st.write("---")
    st.write("Heart Disease Prediction System")
    st.write("Developed by MEHRAN KHAN")
    st.write("© 2026 All Rights Reserved")
footer()


# The code below sets the background image and theme for the Streamlit app
st.markdown("""
<style>

.stApp{
background:
linear-gradient(rgba(15,23,42,.85),rgba(15,23,42,.85)),
url("https://images.unsplash.com/photo-1526778548025-fa2f459cd5c1?auto=format&fit=crop&w=1920&q=80");

background-size:cover;
background-position:center;
background-attachment:fixed;
}

.block-container{
background:rgba(255,255,255,.80);
padding:45px;
border-radius:22px;
box-shadow:0 15px 40px rgba(0,0,0,.95);
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


/* ===========================
   Top Header Buttons
   (Deploy, Menu, etc.)
=========================== */
header[data-testid="stHeader"]{
    background: transparent !important;
}


header[data-testid="stHeader"] button{
    color: white !important;
}

header[data-testid="stHeader"] svg{
    fill: black !important;
    color: black !important;
}

/* Deploy Button */
header[data-testid="stHeader"] .stButton button{
    color: black !important;
    border-color: black !important;
}
/* ===========================
   Three Dots Menu
=========================== */

/* Three-dot icon */
button[aria-label="Main menu"] svg,
button[data-testid="stMainMenuButton"] svg{
    fill: black !important;
    color: black !important;
}

/* Fallback for any header SVG icons */
header[data-testid="stHeader"] button svg{
    fill: white !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
div.block-container{
    padding-top:1rem;
}
</style>
""", unsafe_allow_html=True)



