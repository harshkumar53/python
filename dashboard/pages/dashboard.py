import streamlit as st
import pandas as pd 
import plotly.express as px
import seaborn as sns

st.markdown("<h1 style='color:cyan;'>Titanic Dashboard</h1>", unsafe_allow_html=True)
st.write('This is a Dashboard for analysing the titanic datset')

df = sns.load_dataset('titanic')
st.dataframe(df)


st.sidebar.header('Filtter Options')
# filters

Gender = st.sidebar.multiselect('Gender',
                               options = df['sex'].unique(),
                               default = df['sex'].unique())


pclass = st.sidebar.multiselect('Passenger class',
                               options = df['class'].unique(),
                               default = df['class'].unique())

min_age, max_age = st.sidebar.slider('Age',
                               min_value = int(df['age'].min()),
                               max_value = int(df['age'].max()),
                               value = (int(df['age'].min()), int(df['age'].max())))

# checking the variable is in filterd variable

filtered_df = df[
    (df['sex'].isin(Gender)) &
    (df['class'].isin(pclass)) &
    (df['age']>=(min_age)) &
    (df['age']<=(max_age))
]

# connet to filterd value

fig = px.histogram(filtered_df, x='age',
                   title='Age Distribution',
                   template='plotly_dark')

st.plotly_chart(fig)
st.title('Highest count : 54 of age group 24')
st.markdown('This graph showes the distribution of age of the people')


