import streamlit as st
import numpy as np
import pandas as pd

st.title("Simulación de emisión de partículas (Poisson)")

# entradas del usuario
media_total = st.number_input(
    "Ingrese la media de partículas en el tiempo total (λ):",
    min_value=0.1, value=5.0, step=0.1
)

tiempo_total = st.number_input(
    "Ingrese el tiempo total de simulación:",
    min_value=0.1, value=10.0, step=0.1
)

unidad = st.selectbox("Seleccione la unidad de tiempo:", ["segundos", "minutos", "años"])

if st.button("Generar simulación"):
    # tasa de emisión por unidad de tiempo
    lmbda = media_total / tiempo_total

    # simulación
    interarrivals = []
    t = 0.0
    while True:
        dt = np.random.exponential(1/lmbda)
        if t + dt > tiempo_total:
            break
        t += dt
        interarrivals.append(dt)

    # tiempos acumulados
    tiempos_acumulados = np.cumsum(interarrivals)

    # resultados en tabla
    df = pd.DataFrame({
        "Partícula": np.arange(1, len(interarrivals)+1),
        f"Tiempo entre partículas ({unidad})": interarrivals,
        f"Tiempo acumulado ({unidad})": tiempos_ac_
