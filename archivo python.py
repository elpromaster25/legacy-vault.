import streamlit as st
import pandas as pd
import time

# --- 1. LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'demo' not in st.session_state: st.session_state.demo = False
if 'start_time' not in st.session_state: st.session_state.start_time = None
if 'mensajes' not in st.session_state: st.session_state.mensajes = []

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY QUANTUM VAULT", layout="wide")
st.markdown("<style>.stApp { background-color: #000000; border: 6px solid #d4af37; padding: 25px; } h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; } [data-testid='stMetricValue'] { color: #d4af37 !important; font-size: 3.5rem !important; } .vip-banner { background: linear-gradient(90deg, #b8860b, #d4af37, #f7e08b); color: black !important; padding: 15px; text-align: center; font-weight: bold; border-radius: 10px; margin-bottom: 20px; }</style>", unsafe_allow_html=True)

# --- 3. ACCESO (LOGIN/DEMO) ---
if not st.session_state.auth and not st.session_state.demo:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    st.markdown("<div style='color: #d4af37; text-align: center; border: 2px solid #d4af37; padding: 20px;'>💎 ACCESO VIP: 2.000.000 ARS / 12.000 USD</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔑 LLAVE MAESTRA"): st.session_state.auth = "login_form"; st.rerun()
    with c2:
        if st.button("🚀 DEMO (5 MIN)"): st.session_state.demo = True; st.session_state.start_time = time.time(); st.rerun()
    st.stop()

# --- 4. FORMULARIO LOGIN ---
if st.session_state.auth == "login_form":
    st.subheader("🔐 VALIDACIÓN VIP")
    password = st.text_input("PASSWORD:", type="password")
    if st.button("ENTRAR"):
        if password == "LEGACY2026": st.session_state.auth = True; st.rerun()
        else: st.error("DENEGADO")
    st.stop()

# --- 5. CONTROL DEMO ---
if st.session_state.demo and not st.session_state.auth:
    if (time.time() - st.session_state.start_time) > 300:
        st.title("⌛ EXPIRADO"); st.markdown("<div class='vip-banner'>PAGUE 2 MILLONES PARA CONTINUAR</div>", unsafe_allow_html=True)
        if st.button("INICIO"): st.session_state.demo = False; st.rerun()
        st.stop()

# --- 6. COMMAND CENTER (TABLERO REAL) ---
if st.session_state.auth == True:
    st.markdown("<div class='vip-banner'>💎 BIENVENIDO DYLAN GARCÍA | ESTADO: VIP</div>", unsafe_allow_html=True)

# --- TU BOTÓN DE ESPÍA (MODO ADMIN) ---
# Ponemos una contraseña interna para que nadie más lo abra
if st.sidebar.text_input("🕵️ MODO ESPÍA (CONTRA):", type="password") == "DYLAN777":
    st.title("👨‍💻 PANEL DE INTELIGENCIA")
    st.subheader("📬 Mensajes de Empresarios:")
    if st.session_state.mensajes: st.table(pd.DataFrame(st.session_state.mensajes))
    else: st.info("Aún no hay mensajes. ¡Tené paciencia, CEO!")
    st.write("---")

st.title("🏛️ COMMAND CENTER LEGACY")
if st.session_state.demo: st.warning(f"⚠️ MODO DEMO: {int(300 - (time.time() - st.session_state.start_time))}s")

# SIMULADOR Y MÉTRICAS
años = st.slider("PROYECCIÓN (AÑOS):", 1, 30, 10); ret = st.slider("RENTABILIDAD (%):", 5, 50, 15)
fut_usd = 12450000 * ((1 + (ret/100))**años)
m1, m2 = st.columns(2)
m1.metric("VALOR USD", f"${fut_usd:,.0f}"); m2.metric("VALOR ARS", f"${(fut_usd * 1500):,.0f}")

st.write("---")
c1, c2 = st.columns(2)
with c1:
    st.subheader("📊 ACTIVOS VIP")
    df = pd.DataFrame({"Activo": ["Propiedades", "Stocks", "Crypto", "Art"], "Valor": [40, 30, 20, 10]})
    st.bar_chart(df.set_index("Activo"))
with c2:
    st.subheader("🤖 IA VIP")
    q = st.text_input("CONSULTA:")
    if q: st.write("🏛️ **IA:** Analizando... La orden estratégica es MANTENER POSICIONES.")

if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False; st.session_state.demo = False; st.rerun()
