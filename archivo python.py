import streamlit as st
import time

# --- 1. LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL (CENTRADO FORZADO) ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label { color: #d4af37 !important; text-align: center !important; }
    
    /* FORZAR CENTRADO DE MÉTRICAS */
    [data-testid="stMetric"] { text-align: center !important; display: flex; flex-direction: column; align-items: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.8rem !important; }
    
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; }
    .stTextInput > div > div > input { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ACCESO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    _, col_ce, _ = st.columns([1, 1.5, 1])
    with col_ce:
        emp = st.text_input("IDENTIFIQUE SU FIRMA:", key="e_final")
        pw = st.text_input("MASTER KEY:", type="password", key="p_final")
        if st.button("🔓 DESBLOQUEAR"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp.upper()
                st.session_state.auth = True
                st.rerun()
            else: st.error("Datos requeridos.")
    st.stop()

# --- 4. INTERIOR (TODO RESTAURADO Y CENTRADO) ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")
st.write("---")

# MÉTRICAS (3 COLUMNAS SIMPLES)
c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$145M" if "GINEVRA" in emp else "$85M")
with c2: st.metric("YACHTS", "$25M" if "GINEVRA" in emp else "$12.5M")
with c3: st.metric("JETS", "$40M" if "GINEVRA" in emp else "$24M")

st.write("---")

# IA ESTRATÉGICA
st.subheader(f"🤖 ESTRATEGA IA PARA {emp}")
_, col_ia, _ = st.columns([0.5, 2, 0.5])
with col_ia:
    pregunta = st.text_input("CONSULTA TÉCNICA:", key="q_ia")
    if pregunta:
        with st.spinner("Analizando..."):
            time.sleep(1)
            st.markdown(f"<div class='gold-card'>🏛️ <b>IA ADVISOR:</b> Director de {emp}, análisis completado. Sugerimos <b>MANTENER POSICIONES</b>.</div>", unsafe_allow_html=True)

st.write("---")

# SCANNER QUÁNTICO
st.subheader("🧬 SCANNER DE ACTIVOS")
_, col_sc, _ = st.columns([0.5, 2, 0.5])
with col_sc:
    st.text_area("LISTA DE PROPIEDADES:", key="sc_ia")
    if st.button("ANALIZAR LISTA"): st.success("Escaneo finalizado.")

st.write("---")

# RELOJES MUNDIALES
r1, r2, r3 = st.columns(3)
with r1: st.markdown("<div class='gold-card'>🗽 NY: 11:30 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 01:30 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 04:30 AM</div>", unsafe_allow_html=True)

if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False
    st.rerun()
