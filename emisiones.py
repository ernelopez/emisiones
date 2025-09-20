# app.py
import streamlit as st
import numpy as np
import pandas as pd

st.title("Simulación de emisión de partículas (Poisson)")

# entradas del usuario
media_total = st.number_input(
    "Ingrese la media de partículas en el tiempo total (λ):",
    min_value=0.1, value=5.0, step=0.1
)

T_total = st.number_input(
    "Ingrese el tiempo total de simulación:",
    min_value=0.1, value=10.0, step=0.1
)

unidad = st.selectbox("Seleccione la unidad de tiempo:", ["segundos", "minutos", "años"])

# factor de conversión a segundos (opcional, según unidad)
if st.button("Generar simulación"):
    # convertir tiempo total a segundos si es necesario (solo para mostrar)
    if unidad == "segundos":
        T = T_total
    elif unidad == "minutos":
        T = T_total
    elif unidad == "años":
        T = T_total

    # tasa de emisión por unidad de tiempo
    lmbda = media_total / T_total

    # simulación
    interarrivals = []
    t = 0.0
    while True:
        dt = np.random.exponential(1/lmbda)
        if t + dt > T_total:
            break
        t += dt
        interarrivals.append(dt)

    # tiempos acumulados
    tiempo
