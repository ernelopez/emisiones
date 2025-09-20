# archivo: app.py
import streamlit as st
import numpy as np
import pandas as pd

st.title("Simulación de emisión de partículas (Poisson)")

# entrada del usuario
media_10s = st.number_input(
    "Ingrese la media de partículas en 10 segundos (λ):",
    min_value=0.1, value=5.0, step=0.1
)

if st.button("Generar simulación"):
    # parámetros
    T_total = 10.0
    lmbda = media_10s / T_total

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
    tiempos_acumulados = np.cumsum(interarrivals)

    # resultados en tabla
    df = pd.DataFrame({
        "Partícula": np.arange(1, len(interarrivals)+1),
        "Tiempo entre partículas": interarrivals,
        "Tiempo acumulado": tiempos_acumulados
    })

    st.write(f"Cantidad de partículas emitidas: {len(interarrivals)}")
    st.dataframe(df)
