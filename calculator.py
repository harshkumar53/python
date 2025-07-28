import streamlit as st
# streamlit run calculator.py, this commanad for when ths dic is root dic

st.title('sample calculator')

# st.subheader('this is a syb heading')
# st.markdown('normal paragraph')

# fnum = st.number_input('enter the frist number', value = 0)
# snum = st.number_input('enter the second number', value = 0)



c1,c2 = st.columns(2)

fnum = c1.number_input('enter the frist number', value = 0)
snum = c2.number_input('enter the second number', value = 0)


choice = ['Add','Sub', 'Mul','Div']
st.subheader('Option')
option = st.radio('select any one option',choice)

button = st.button('calculate')
result = 0

if button:
    if option == 'Add':
        result = fnum+snum
    if option == 'Sub':
        result = fnum-snum
    if option == 'Mul':
        result = fnum*num
    if option == 'Div':
        result = fnum/snum

st.success(f'result is {result}: ')