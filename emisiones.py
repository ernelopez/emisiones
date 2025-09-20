# app.py
import streamlit as st
import numpy as np
import pandas as pd

st.title("Simulación de decaimiento de C-14 (Proceso de Poisson)")

# entradas del usuario
N0 = st.number_input("Número de átomos iniciales:", min_value=1, value=10, step=1)
t_half = st.number_input("Vida media (t_1/2):", min_value=0.1, value=5730.0, step=1.0)
tiempo_total = st.number_input("Tiempo total de simulación:", min_value=0.1, value=5730.0, step=1.0)
unidad = st.selectbox("Unidad de tiempo:", ["años", "segundos", "minutos"])

if st.button("Generar simulación"):
    # constante de decaimiento
    lmbda = np.log(2)/t_half

    # simulación de tiempos de decaimiento para cada átomo
    tiempos_decaimiento = np.random.exponential(1/lmbda, size=N0)

    # ordenamos los tiempos
    tiempos_acumulados = np.sort(tiempos_decaimiento)

    # tabla de resultados
    df = pd.DataFrame({
        "Átomo": np.arange(1, N0+1),
        f"Tiempo de decaimiento ({unidad})": tiempos_acumulados
    })

    # número de átomos que decaen antes del tiempo total
    decaidos = np.sum(tiempos_acumulados <= tiempo_total)

    st.write(f"Número total de átomos simulados: {N0}")
    st.write(f"Número esperado de decaimientos en {tiempo_total} {unidad}: {N0* (1 - np.exp(-lmbda * tiempo_total)):.1f}")
    st.write(f"Número de átomos que decaen antes de {tiempo_total} {unidad}: {decaidos}")
    st.dataframe(df)
