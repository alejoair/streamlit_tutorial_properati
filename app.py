import streamlit as st
from pickle import load
import numpy as np

st.title("Properati")

if st.button("Cargar modelo"):
	st.model = load(open("modelo.pkl", "rb"))
	st.write(st.model)


habitaciones = st.selectbox("Numero de habitaciones", [1, 2, 3, 4, 5, 6])
banios = st.selectbox("Numero de baños", [1, 2, 3, 4, 5, 6])
area = st.number_input("Superficie en m2")


if st.button("Hacer prediccion"):

	data = np.array([habitaciones, banios, area]).reshape(1, -1)
	pred = st.model.predict(data)

	st.write("El precio es de: {:.0f}".format(pred[0]))