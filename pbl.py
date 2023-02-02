import streamlit as st
import numpy as np
import altair as alt
import pandas as pd



st.write("HII JUYSS")


st.header('PROJECT BASED LEARNING I')

if st.button('Welcome to our project'):
    st.write('Data analytics and Machine learning')
else:
    st.write('Goodbye')




st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     "Linkedin Id": [1, 2, 3, 4],
     "Job Vacancies": [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)