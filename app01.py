import streamlit as st
import pandas as pd
import numpy as np
 
st.title('จารุวิทย์ คำพันธ์ 66114540131')
import streamlit as st
import pandas as pd


st.write("This is introduction to streamlit")

st.markdown("## Code")
code = '''
def hello():
    print("Hello!")
'''

show_btn = st.button("Show code!")
if show_btn:
    st.code(code, language='python')


cols = st.columns(2)
with cols[0]:
    age_inp = st.number_input("Input your age")
    st.markdown(f"Your age is {round(age_inp, 2)}")


# st.markdown("# NLP Task")
with cols[1]:
    text_inp = st.text_input("Input your text")
    word_tokenize = "|".join(text_inp.split())
    st.markdown(f"{word_tokenize}")


df = pd.DataFrame({
'first column': [1, 2, 3, 4],
'second column': [10, 20, 60, 90]
})
st.dataframe(df)
show_chart_btn = st.button("Show Chart!!")
if show_chart_btn:
    st.line_chart(df, x='first column', y='second column')