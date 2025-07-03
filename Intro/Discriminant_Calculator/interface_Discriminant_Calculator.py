
from Discriminant_Calculator import *
import streamlit as st

st.title("Discriminant Calculator")
st.write("This app calculates the discriminant of a quadratic equation of the form:")

st.markdown(r"### 🧪 Equation")
st.markdown(r"$ax^2 + bx + c = 0$")


a = st.number_input("Enter coefficient a:", value=0.0)
b = st.number_input("Enter coefficient b:", value=0.0)
c = st.number_input("Enter coefficient c:", value=0.0)

if st.button("Calculate"):
    delta_value = Delta(a, b, c)
    Roots(delta_value, a, b, c)
