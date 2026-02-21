import streamlit as st
import time

# --- 1. LÓGICA DE IDENTIDAD DINÁMICA ---
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY | DYNAMIC VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center; }
    .gold-card { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ACCESO (EL CAPTURADOR) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        # AQUÍ CAPTURAMOS LA EMPRESA
        empresa = st.text_input("IDENTIFIQUE SU FIRMA / COMPANY:", placeholder="Ej: GINEVRA, REMAX, L.J. RAMOS", key="e_dyn")
        pw = st.text_input("MASTER KEY:", type="password", key="p_dyn")
        if st.button("🔓 DESBLOQUEAR"):
            if pw == "LEGACY2026" and empresa:
                st.session_state.emp_final = empresa.upper()
                st.session_state.auth = True; st.rerun()
            else: st.error("Identificación requerida para encriptación.")
    st.stop()

# --- 4. INTERIOR 100% PERSONALIZADO (LA MAGIA) ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")
st.write("---")

# --- LÓGICA DE DATOS SEGÚN LA EMPRESA ---
# Si es una de las grandes, le mostramos "sus" supuestos activos
if "GINEVRA" in emp:
    val_re, val_ya, val_jet = "$145,000,000", "$25,000,000", "$40,000,000"
    msg_ia = f"Análisis de Madero Harbour completado. Sugerimos expandir flota corporativa."
elif "REMAX" in emp:
    val_re, val_ya, val_jet = "$920,000,000", "$10,000,000", "$15,000,000"
    msg_ia = f"Cartera de agentes Remax analizada. Optimización de comisiones en curso."
else:
    # Datos estándar para cualquier otro
    val_re, val_ya, val_jet = "$85,000,000", "$12,500,000", "$24,000,000"
    msg_ia = f"Análisis patrimonial para {emp} finalizado. Estado: SOLVENTE."

# MOSTRAR MÉTRICAS PERSONALIZADAS
c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE ASSETS", val_re)
with c2: st.metric("YACHTS & MARINE", val_ya)
with c3: st.metric("FLIGHT OPERATIONS", val_jet)

st.write("---")
# IA HABLANDO DIRECTO AL CLIENTE
st.subheader(f"🤖 ESTRATEGA IA PARA {emp}")
st.info(f"🏛️ **IA ADVISOR:** {msg_ia}")

st.write("---")
# RELOJES MUNDIALES
r1, r2, r3 = st.columns(3)
with r1: st.markdown("<div class='gold-card'>🗽 NY: 11:27 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 01:27 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 04:27 AM</div>", unsafe_allow_html=True)

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
