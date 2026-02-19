import streamlit as st
import pandas as pd

# 1. EL CEREBRO DE LA BÓVEDA (Seguridad)
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.markdown("<style>.stApp { background-color: #0e1117; } h1 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    st.title("🔐 ACCESO EXCLUSIVO LEGACY")
    password = st.text_input("CLAVE DE ACCESO:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA"):
        if password == "LEGACY2026":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Clave Incorrecta.")
    st.stop()

# 2. TU DISEÑO DE LUJO (Lo que se ve después del Login)
st.set_page_config(page_title="LEGACY VAULT VIP", page_icon="🗝️", layout="wide")
st.markdown("<style>.stApp { background-color: #0e1117; } h1, h3 { color: #d4af37; text-align: center; } .stMarkdown p { color: white; }</style>", unsafe_allow_html=True)

st.title("🗝️ LEGACY VAULT")
st.markdown("<h3 style='color: white;'>Patrimonio de Alta Gama</h3>", unsafe_allow_html=True)

# 3. Datos y Gráficos
data = {"Activo": ["Inmuebles", "Acciones", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]}
df = pd.DataFrame(data)
st.metric(label="VALOR NETO TOTAL", value="$12,450,000 USD", delta="+2.4%")
st.bar_chart(df.set_index("Activo"))

# 4. LA IA ESTRATÉGICA (¡Acá volvió!) 🤖
st.markdown("---")
st.subheader("🤖 LEGACY AI: Consultoría Privada")
pregunta = st.text_input("¿En qué activo desea invertir hoy?")

if pregunta:
    with st.spinner('Consultando base de datos...'):
        if "mendoza" in pregunta.lower():
            st.write("🏛️ **LEGACY AI:** Excelente elección. La tierra en Mendoza es el activo más estable de la región.")
        else:
            st.write(f"🏛️ **LEGACY AI:** He analizado su consulta sobre '{pregunta}'. La recomendación es diversificar y mantener el 10% en reserva líquida.")

# 5. Cerrar Sesión
if st.sidebar.button("🔒 CERRAR BÓVEDA"):
    st.session_state.autenticado = False
    st.rerun()
