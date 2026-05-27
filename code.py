import streamlit as st
st.title('WELCOME TO FIRST STREAMLIT PROJECT BY RAJ VISHWAKARMA !!')
st.write('THIS APP CALCULATES THE SQUARE OF THE NUMBER.')
st.header('SELECT A NUMBER')
number =  st.slider("PICK A NUMBER", 0,100,25) #min,max,default
st.subheader("RESULTS")
sq_num= number * number
st.write("The square value of {} is {}", number,sq_num)
