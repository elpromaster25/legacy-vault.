import streamlit as st
import pandas as pd
import time

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="LEGACY QUANTUM VAULT", page_icon="🏛️", layout="wide")

# --- 2. LÓGICA DE ACCESO ---
if 'auth' not in st.session_state:
    st.session_state.auth = False
if 'demo' not in st.session_state:
    st.session_state.demo = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

# --- 3. ESTILO DORADO ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    [data-testid='stMetricValue'] { color: #d4af37 !important; font-size: 3rem !important; font-weight: bold; }
    .gold-box { border: 2px solid #d4af37; padding: 20px; border-radius: 10px; text-align: center; color: #d4af37; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. PANTALLA DE ENTRADA ---
if not st.session_state.auth and not st.session_state.demo:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    st.write("---")
    st.markdown("<div class='gold-price' style='color: #d4af37; text-align: center; font-size: 1.5rem; font-weight: bold;'>🇦🇷 ARGENTINA: 2 MILLONES / MES<br>🇺🇸 USA: 12 THOUSAND USD / MONTH</div>", unsafe_allow_html=True)
    st.write("")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔑 INGRESAR CON LLAVE MAESTRA"):
            st.session_state.auth = "login_form"
            st.rerun()
    with c2:
        if st.button("🚀 INICIAR DEMO GRATUITA (5 MIN)"):
            st.session_state.demo = True
            st.session_state.start_time = time.time()
            st.rerun()
    st.stop()

# --- 5. FORMULARIO DE LOGIN ---
if st.session_state.auth == "login_form":
    st.subheader("🔐 INGRESE LLAVE MAESTRA")
    password = st.text_input("PASSWORD:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA"):
        if password == "LEGACY2026":
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("ACCESO DENEGADO")
    st.stop()

# --- 6. CONTROL DE TIEMPO DEMO ---
if st.session_state.demo and not st.session_state.auth:
    elapsed = time.time() - st.session_state.start_time
    if elapsed > 300: 
        st.title("⌛ TIEMPO DE DEMO EXPIRADO")
        st.markdown("<div class='gold-box'>PARA CONTINUAR DEBE ADQUIRIR SU LLAVE VIP.<br>COSTO: 2.000.000 ARS / 12K USD</div>", unsafe_allow_html=True)
        if st.button("VOLVER AL INICIO"):
            st.session_state.demo = False
            st.session_state.start_time = None
            st.rerun()
        st.stop()

# --- 7. PANEL DE CONTROL FINAL ---
st.title("🏛️ COMMAND CENTER LEGACY")
if st.session_state.demo:
    st.warning(f"⚠️ MODO DEMO ACTIVO: {int(300 - (time.time() - st.session_state.start_time))} segundos restantes")

años = st.slider("PROYECCIÓN PATRIMONIAL (AÑOS):", 1, 30, 10)
ret = st.slider("RENTABILIDAD ANUAL ESTIMADA (%):", 5, 50, 15)
capital_base = 12450000
futuro_usd = capital_base * ((1 + (ret/100))**años)

st.write("---")
m1, m2 = st.columns(2)
m1.metric("VALOR PROYECTADO USD", f"${futuro_usd:,.0f}")
m2.metric("VALOR PROYECTADO ARS", f"${(futuro_usd * 1500):,.0f}")

st.write("---")
c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 DISTRIBUCIÓN DE ACTIVOS")
    # --- AQUÍ ESTÁ EL ARREGLO DE LOS VALORES ---
    datos_graficos = pd.DataFrame({
        "Activo": ["Propiedades", "Stocks", "Crypto", "Arte"],
        "Valor": [45, 25, 20, 10]
    })
    st.bar_chart(datos_graficos.set_index("Activo"))

with c2:
    st.subheader("🤖 ESTRATEGA IA")
    pregunta = st.text_input("CONSULTA TÉCNICA A LA IA:")
    if pregunta:
        with st.spinner('Analizando...'):
            time.sleep(1)
            st.write(f"🏛️ **IA:** Dylan García, para la consulta '{pregunta}', el análisis sugiere MANTENER POSICIONES.")

if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False
    st.session_state.demo = False
    st.rerun()
