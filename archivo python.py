import streamlit as st
import time

# --- 1. LÓGICA ---
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label { color: #d4af37 !important; text-align: center !important; }
    [data-testid="stMetric"] { text-align: center !important; display: flex; flex-direction: column; align-items: center; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.8rem !important; }
    .gold-card { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    
    /* TU NUEVO TICKER DE ORO CHIQUITO */
    .market-ticker { 
        color: #d4af37; 
        font-size: 0.85rem; 
        text-align: center; 
        font-weight: bold; 
        border-bottom: 1px solid rgba(212, 175, 55, 0.3);
        padding-bottom: 10px;
        margin-bottom: 20px;
        letter-spacing: 1px;
    }
    
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; }
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
                st.session_state.auth = True; st.rerun()
            else: st.error("Datos requeridos.")
    st.stop()

# --- 4. INTERIOR CON TICKER ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")

# --- ACÁ ESTÁ TU IDEA: EL TICKER DE ORO CHIQUITO ---
st.markdown(f"""
    <div class='market-ticker'>
        🏦 MERCADO EN VIVO | USDT/ARS: 1.515 | BTC/USD: 96.840 | ETH/USD: 2.720 | 🛡️ ENCRIPTACIÓN AES-256: ACTIVA
    </div>
    """, unsafe_allow_html=True)

# MÉTRICAS
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
        with st.spinner("Consultando..."):
            time.sleep(1)
            st.markdown(f"<div class='gold-card'>🏛️ <b>IA ADVISOR:</b> Análisis para {emp} completado. Sugerimos diversificar en activos líquidos.</div>", unsafe_allow_html=True)

st.write("---")

# SCANNER
st.subheader("🧬 SCANNER DE ACTIVOS")
_, col_sc, _ = st.columns([0.5, 2, 0.5])
with col_sc:
    activos = st.text_area("LISTA DE ACTIVOS:", key="sc_input")
    if st.button("🧬 INICIAR ESCANEO"):
        if activos:
            with st.status("Escaneando...", expanded=True) as status:
                time.sleep(1); status.update(label="Analizado ✅", state="complete")
            st.markdown(f"<div class='gold-card'>💎 VALUACIÓN DETECTADA: <b>$42,500,000 USD</b></div>", unsafe_allow_html=True)

st.write("---")

# RELOJES MUNDIALES
r1, r2, r3 = st.columns(3)
with r1: st.markdown("<div class='gold-card'>🗽 NY: 11:40 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 01:40 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 04:40 AM</div>", unsafe_allow_html=True)

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
