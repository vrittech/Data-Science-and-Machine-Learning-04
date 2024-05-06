import streamlit as st

st.title("Hello Everyone !")

sl = st.number_input("Enter Sepal Length")
sw = st.number_input("Enter Sepal Width")
pl = st.number_input("Enter Petal Length")
pw = st.number_input("Enter Petal Width")

st.write(f"Sum of Numbers : {sl+sw+pl+pw}")