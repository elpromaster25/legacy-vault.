import streamlit as st
import pandas as pd
import time

# --- 1. CONFIGURACIÓN DE CRONÓMETRO (DEMO) ---
if 'inicio_demo' not in st.session_state:
    st.session_state.inicio_demo = None
if 'demo_terminada' not in st.session_state:
    st.session_state.demo_terminada = False
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False

# --- 2. PANTALLA DE ENTRADA (EL FILTRO) ---
if not st.session_state.autenticado and not st.session_state.inicio_demo:
    st.set_page_config(page_title="LEGACY | ACCESO", page_icon="🔐", layout="wide")
    st.markdown("<style>.stApp { background-color: #000000; } h1, h2 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    st.title("🏛️ LEGACY QUANTUM VAULT")
    
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        st.subheader("Seleccione su vía de acceso:")
        if st.button("🔑 INGRESAR CON LLAVE MAESTRA"):
            st.session_state.autenticado = "login_form"
            st.rerun()
        
        st.write("---")
        if st.button("🚀 INICIAR DEMO GRATUITA (5 MIN)"):
            st.session_state.inicio_demo = time.time()
            st.rerun()
    st.stop()

# --- 3. LÓGICA DE BLOQUEO POR TIEMPO ---
if st.session_state.inicio_demo and not st.session_state.autenticado:
    tiempo_transcurrido = time.time() - st.session_state.inicio_demo
    if tiempo_transcurrido > 300: # 300 segundos = 5 minutos
        st.session_state.demo_terminada = True

# --- 4. MURO DE PAGO (CUANDO SE ACABA EL TIEMPO) ---
if st.session_state.demo_terminada and not st.session_state.autenticado:
    st.set_page_config(page_title="TIEMPO EXPIRADO", page_icon="🚫")
    st.markdown("<style>.stApp { background-color: #000000; } h1, h3 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    st.title("⌛ SU TIEMPO DE DEMO HA EXPIRADO")
    
    # DETECTOR DE PAÍS PARA EL PAGO
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div style='border: 2px solid #d4af37; padding: 20px; text-align: center;'>🇦🇷 ARGENTINA<br><h3>Pagar 2 Millones ARS/mes</h3></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='border: 2px solid #d4af37; padding: 20px; text-align: center;'>🇺🇸 USA / INT<br><h3>Pay 12 Thousand USD/month</h3></div>", unsafe_allow_html=True)
    
    st.write("---")
    if st.button("⬅️ VOLVER AL INICIO E INICIAR SESIÓN"):
        st.session_state.inicio_demo = None
        st.session_state.demo_terminada = False
        st.rerun()
    st.stop()

# --- 5. FORMULARIO DE LOGIN (SI ELIGE LLAVE) ---
if st.session_state.autenticado == "login_form":
    password = st.text_input("INGRESE LLAVE MAESTRA:", type="password")
    if st.button("DESBLOQUEAR"):
        if password == "LEGACY2026":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("LLAVE INVÁLIDA")
    st.stop()

# --- 6. INTERFAZ PRINCIPAL (EL PRODUCTO) ---
st.set_page_config(page_title="LEGACY COMMAND", layout="wide")
st.markdown("<style>.stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; }</style>", unsafe_allow_html=True)

if st.session_state.inicio_demo:
    st.warning(f"⚠️ MODO DEMO ACTIVO. Tiempo restante: {int(300 - (time.time() - st.session_state.inicio_demo))} segundos.")

st.title("🏛️ COMMAND CENTER LEGACY")
# (Aquí sigue tu simulador de billones, IA y gráficos...)
st.write("PATRIMONIO TOTAL: $12.450.000 USD")
df = pd.DataFrame({"Activo": ["RE", "Stocks", "Crypto", "Art"], "Valor":})
st.bar_chart(df.set_index("Activo"))

if st.sidebar.button("🔒 SALIR"):
    st.session_state.autenticado = False
    st.session_state.inicio_demo = None
    st.rerun()
