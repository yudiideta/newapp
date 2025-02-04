import streamlit as st
import random

st.title("Simulador de Lançamento de Moeda")

num_lancamentos = st.number_input("Quantas vezes deseja lançar a moeda?", min_value=1, step=1, value=1)

if st.button("Lançar Moeda"):
    resultados = [random.choice(["Cara", "Coroa"]) for _ in range(num_lancamentos)]
    st.write(f"Resultados: {', '.join(resultados)}")

