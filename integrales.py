import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify, integrate

# Título de la app
st.title("📈 Calculadora de Integrales Definidas con Gráfico")

# Ingreso de función y límites
st.markdown("Introduce la función a integrar y los límites:")

# Inputs del usuario
funcion_str = st.text_input("🔹 Función f(x):", value="x**2")
a = st.number_input("🔹 Límite inferior (a):", value=0.0)
b = st.number_input("🔹 Límite superior (b):", value=2.0)

# Procesar la integral al presionar botón
if st.button("Calcular integral"):
    try:
        # Símbolo
        x = symbols('x')

        # Convertir string a expresión simbólica
        funcion = sympify(funcion_str)

        # Calcular integral simbólica y numérica
        integral_definida = integrate(funcion, (x, a, b))

        # Mostrar resultado
        st.success(f"📐 Valor de la integral entre {a} y {b}: {integral_definida.evalf():.4f}")

        # Preparar gráfico
        f_lambd = lambdify(x, funcion, modules=["numpy"])
        x_vals = np.linspace(a, b, 300)
        y_vals = f_lambd(x_vals)

        # Dibujar área bajo la curva
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=f"f(x) = {funcion_str}", color='blue')
        ax.fill_between(x_vals, y_vals, color='skyblue', alpha=0.4)
        ax.axhline(0, color='black', linewidth=0.8)
        ax.legend()
        ax.set_title("Área bajo la curva")

        st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Error al procesar la función: {e}")