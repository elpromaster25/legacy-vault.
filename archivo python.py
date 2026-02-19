import streamlit as st
import pandas as pd

# 1. EL CEREBRO DE LA BÓVEDA (Contraseña)
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

# --- PANTALLA DE LOGIN ---
if not st.session_state.autenticado:
    st.set_page_config(page_title="LOGIN PRIVADO", page_icon="🔒")
    st.markdown("<style>.stApp { background-color: #0e1117; } h1 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    
    st.title("🔐 ACCESO EXCLUSIVO LEGACY")
    st.markdown("<p style='text-align: center; color: white;'>Ingrese su Clave de Inversor para desbloquear el patrimonio.</p>", unsafe_allow_html=True)
    
    # AQUÍ ELIGES TU CONTRASEÑA (Cámbiala si quieres)
    password = st.text_input("CLAVE DE ACCESO:", type="password")
    
    if st.button("DESBLOQUEAR BÓVEDA"):
        if password == "LEGACY2026": # <--- ESTA ES TU LLAVE
            st.session_state.autenticado = True
            st.success("Acceso Concedido. Cargando activos...")
            st.rerun()
        else:
            st.error("Clave Incorrecta. Intento reportado al sistema de seguridad.")
    st.stop()

# 2. TU DISEÑO DE LUJO (Lo que se ve después del Login)
st.set_page_config(page_title="LEGACY VAULT VIP", page_icon="🗝️", layout="wide")
st.markdown("<style>.stApp { background-color: #0e1117; } h1, h3 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)

st.title("🗝️ LEGACY VAULT")
st.markdown("<h3 style='color: white;'>Panel de Control de Activos</h3>", unsafe_allow_html=True)

# Datos de la fortuna
data = {"Activo": ["Inmuebles", "Acciones", "Cripto", "Arte"], "Valor": [60, 20, 10, 10]}
df = pd.DataFrame(data)
st.metric(label="VALOR NETO TOTAL", value="$12,450,000 USD")
st.bar_chart(df.set_index("Activo"))

if st.sidebar.button("CERRAR SESIÓN"):
    st.session_state.autenticado = False
    st.rerun()
