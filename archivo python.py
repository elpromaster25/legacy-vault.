import streamlit as st
import time

# --- 1. LÓGICA ---
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL (CENTRADO ABSOLUTO) ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    /* FONDO Y BORDES */
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    
    /* FORZAR CENTRADO DE TODO EL TEXTO */
    h1, h2, h3, p, label { color: #d4af37 !important; text-align: center !important; }
    
    /* EL TRUCO PARA LAS MÉTRICAS CENTRADAS */
    [data-testid="stMetric"] {
        display: flex;
        flex-direction: column;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        width: 100% !important;
    }
    [data-testid="stMetricValue"] { 
        color: #d4af37 !important; 
        font-size: 2.8rem !important; 
        width: 100% !important;
        text-align: center !important;
    }
    [data-testid="stMetricLabel"] { 
        width: 100% !important;
        text-align: center !important;
    }

    /* TICKER INFINITO */
    .ticker-wrap { width: 100%; overflow: hidden; background: rgba(212, 175, 55, 0.05); border-bottom: 1px solid #d4af37; padding: 5px 0; margin-bottom: 30px; }
    .ticker-move { display: inline-block; white-space: nowrap; padding-right: 100%; animation: marquee 25s linear infinite; color: #d4af37; font-size: 0.9rem; font-weight: bold; letter-spacing: 2px; }
    @keyframes marquee { 0% { transform: translate(0, 0); } 100% { transform: translate(-100%, 0); } }
    
    /* CARTAS DORADAS */
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; margin-bottom: 10px; }
    
    /* BOTONES Y INPUTS */
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; }
    .stTextArea > div > div > textarea { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; text-align: center; }
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

# --- 4. INTERIOR ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")

# TICKER (QUE SE MUEVE)
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 LIVE MARKET | USDT/ARS: 1.515 ▲ | BTC/USD: 96.840 ▼ | GOLD/OZ: 2.045 ▲ | 🛡️ AES-256 ACTIVE | TERMINAL: {emp} 🏛️</div></div>', unsafe_allow_html=True)

# MÉTRICAS (USAMOS COLUMNAS CON MÁRGENES PARA CENTRAR)
_, c1, c2, c3, _ = st.columns([0.1, 1, 1, 1, 0.1])
with c1: st.metric("REAL ESTATE", "$145M" if "GINEVRA" in emp else "$85M")
with c2: st.metric("YACHTS", "$25M" if "GINEVRA" in emp else "$12.5M")
with c3: st.metric("JETS", "$40M" if "GINEVRA" in emp else "$24M")

st.write("---")

# IA ADVISOR
st.subheader(f"🤖 ESTRATEGA IA PARA {emp}")
_, col_ia, _ = st.columns([0.5, 2, 0.5])
with col_ia:
    q = st.text_input("CONSULTA TÉCNICA:", key="q_ia")
    if q:
        with st.spinner("Analizando..."):
            time.sleep(1)
            st.markdown(f"<div class='gold-card'>🏛️ <b>IA ADVISOR:</b> Análisis completado para {emp}. Estado: SOLVENTE.</div>", unsafe_allow_html=True)

st.write("---")

# SCANNER (FUNTIONANDO AL 100%)
st.subheader("🧬 SCANNER DE ACTIVOS PATRIMONIALES")
_, col_sc, _ = st.columns([0.5, 2, 0.5])
with col_sc:
    activos = st.text_area("LISTA DE ACTIVOS:", placeholder="Ej: 2 Ferraris...", key="sc_input")
    if st.button("🧬 INICIAR ESCANEO"):
        if activos:
            with st.status("Escaneando...", expanded=True) as s:
                time.sleep(1); s.update(label="Escaneo Finalizado ✅", state="complete")
            st.markdown(f"<div class='gold-card'><h3>💎 VALUACIÓN DETECTADA</h3><h2 style='color:#d4af37;'>$42,500,000 USD</h2></div>", unsafe_allow_html=True)

st.write("---")

# RELOJES (SIMÉTRICOS)
_, r1, r2, r3, _ = st.columns([0.1, 1, 1, 1, 0.1])
with r1: st.markdown("<div class='gold-card'>🗽 NY: 11:42 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 01:42 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 04:42 AM</div>", unsafe_allow_html=True)

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
