import streamlit as st
import time

# --- 1. LÓGICA DE IDENTIDAD ---
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL (CENTRADO TOTAL) ---
st.set_page_config(page_title="LEGACY | SYMMETRY", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    
    /* CENTRADO DE MÉTRICAS */
    [data-testid="stMetricValue"] { text-align: center !important; width: 100% !important; font-size: 2.5rem !important; }
    [data-testid="stMetricLabel"] { text-align: center !important; width: 100% !important; }
    
    .gold-card { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; }
    .stTextInput > div > div > input { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ACCESO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    _, col_ce, _ = st.columns([1, 1.5, 1])
    with col_ce:
        empresa = st.text_input("IDENTIFIQUE SU FIRMA:", placeholder="GINEVRA, REMAX...", key="e_cent")
        pw = st.text_input("MASTER KEY:", type="password", key="p_cent")
        if st.button("🔓 DESBLOQUEAR"):
            if pw == "LEGACY2026" and empresa:
                st.session_state.emp_final = empresa.upper()
                st.session_state.auth = True; st.rerun()
            else: st.error("Datos obligatorios.")
    st.stop()

# --- 4. INTERIOR (COMMAND CENTER SIMÉTRICO) ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")
st.write("---")

# MÉTRICAS CENTRADAS CON COLUMNAS VACÍAS A LOS LADOS
_, c1, c2, c3, _ = st.columns([0.2, 1, 1, 1, 0.2])
with c1: st.metric("REAL ESTATE", "$145M" if "GINEVRA" in emp else "$85M")
with c2: st.metric("YACHTS", "$25M" if "GINEVRA" in emp else "$12.5M")
with c3: st.metric("JETS", "$40M" if "GINEVRA" in emp else "$24M")

st.write("---")

# IA ADVISOR
st.subheader(f"🤖 ESTRATEGA IA PARA {emp}")
_, col_ia, _ = st.columns([0.5, 2, 0.5])
with col_ia:
    pregunta = st.text_input("CONSULTA TÉCNICA O ANÁLISIS DE ACTIVOS:", key="q_cent")
    if pregunta:
        with st.spinner("Consultando..."):
            time.sleep(1)
            st.markdown(f"<div class='gold-card'>🏛️ <b>IA ADVISOR:</b> Director de {emp}, análisis completado. Estado: SOLVENTE.</div>", unsafe_allow_html=True)

st.write("---")
# RELOJES MUNDIALES (IGUAL QUE LAS MÉTRICAS)
_, r1, r2, r3, _ = st.columns([0.2, 1, 1, 1, 0.2])
with r1: st.markdown("<div class='gold-card'>🗽 NY: 11:35 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 01:35 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 04:35 AM</div>", unsafe_allow_html=True)

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
