import streamlit as st
import pandas as pd
import time

# --- 1. LÓGICA DE SESIÓN ---
if 'autenticado' not in st.session_state:
    st.session_state.autenticado = False
if 'inicio_demo' not in st.session_state:
    st.session_state.inicio_demo = None
if 'demo_terminada' not in st.session_state:
    st.session_state.demo_terminada = False

# --- 2. PANTALLA DE ACCESO (LOGIN O DEMO) ---
if not st.session_state.autenticado and not st.session_state.inicio_demo:
    st.set_page_config(page_title="LEGACY | ACCESO", page_icon="🔐", layout="wide")
    st.markdown("<style>.stApp { background-color: #000000; } h1, h2, h3 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    st.title("🏛️ LEGACY QUANTUM VAULT")
    
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        if st.button("🔑 INGRESAR CON LLAVE MAESTRA"):
            st.session_state.autenticado = "form_login"
            st.rerun()
        st.write("---")
        if st.button("🚀 INICIAR DEMO GRATUITA (5 MIN)"):
            st.session_state.inicio_demo = time.time()
            st.rerun()
    st.stop()

# --- 3. FORMULARIO DE LLAVE ---
if st.session_state.autenticado == "form_login":
    st.set_page_config(page_title="LOGIN", page_icon="🔐")
    st.markdown("<style>.stApp { background-color: #000000; } h2 { color: #d4af37; text-align: center; }</style>", unsafe_allow_html=True)
    st.subheader("🔐 INGRESE SU LLAVE")
    pass_input = st.text_input("PASSWORD:", type="password")
    if st.button("DESBLOQUEAR"):
        if pass_input == "LEGACY2026":
            st.session_state.autenticado = True
            st.session_state.inicio_demo = None
            st.rerun()
        else:
            st.error("LLAVE INVÁLIDA")
    st.stop()

# --- 4. CONTROL DE TIEMPO DEMO ---
if st.session_state.inicio_demo and not st.session_state.autenticado:
    if (time.time() - st.session_state.inicio_demo) > 300:
        st.session_state.demo_terminada = True

# --- 5. MURO DE PAGO ---
if st.session_state.demo_terminada and not st.session_state.autenticado:
    st.set_page_config(page_title="EXPIRADO", page_icon="🚫")
    st.markdown("<style>.stApp { background-color: #000000; } h1, h3 { color: #d4af37; text-align: center; border: 2px solid #d4af37; padding: 10px; }</style>", unsafe_allow_html=True)
    st.title("⌛ DEMO FINALIZADA")
    st.write("---")
    c1, c2 = st.columns(2)
    c1.markdown("<h3>🇦🇷 ARGENTINA: 2M ARS</h3>", unsafe_allow_html=True)
    c2.markdown("<h3>🇺🇸 USA: 12K USD</h3>", unsafe_allow_html=True)
    if st.button("VOLVER"):
        st.session_state.inicio_demo = None
        st.session_state.demo_terminada = False
        st.rerun()
    st.stop()

# --- 6. INTERFAZ FINAL ---
st.set_page_config(page_title="LEGACY COMMAND", layout="wide")
st.markdown("<style>.stApp { background-color: #050505; border: 4px solid #d4af37; padding: 20px; } h1, h2, h3 { color: #d4af37 !important; text-align: center; } [data-testid='stMetricValue'] { color: #d4af37 !important; }</style>", unsafe_allow_html=True)

if st.session_state.inicio_demo:
    st.warning(f"⚠️ MODO DEMO. Tiempo restante: {int(300 - (time.time() - st.session_state.inicio_demo))}s")

st.title("🏛️ COMMAND CENTER LEGACY")
años = st.slider("AÑOS:", 1, 30, 10)
ret = st.slider("RETORNO %:", 5, 50, 15)
fut_usd = 12450000 * ((1 + (ret/100))**años)

r1, r2 = st.columns(2)
r1.metric("FORTUNA USD", f"${fut_usd:,.0f}")
r2.metric("FORTUNA ARS", f"${fut_usd * 1500:,.0f}")

st.markdown("---")
c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 ACTIVOS")
    # AQUÍ ESTÁ EL CAMBIO CLAVE: NÚMEROS FIJOS PARA QUE NO DE ERROR
    df_f = pd.DataFrame({"Activo": ["RE", "Stocks", "Crypto", "Art"], "Valor": [40, 30, 20, 10]})
    st.bar_chart(df_f.set_index("Activo"))
with c2:
    st.subheader("🤖 IA")
    q = st.text_input("Consulta:")
    if q: st.write("🏛️ **IA:** Orden estratégica: MANTENER.")

if st.sidebar.button("🔒 SALIR"):
    st.session_state.autenticado = False
    st.session_state.inicio_demo = None
    st.rerun()
