import streamlit as st
import time

# --- 1. LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False

# --- 2. DISEÑO IMPERIAL (CENTRADO Y ANIMADO) ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label { color: #d4af37 !important; text-align: center !important; }
    
    /* CENTRADO DE MÉTRICAS */
    [data-testid="stMetric"] { display: flex; flex-direction: column; align-items: center !important; text-align: center !important; }
    [data-testid="stMetricValue"] { color: #d4af37 !important; font-size: 2.8rem !important; text-align: center !important; }

    /* TICKER INFINITO GLOBAL */
    .ticker-wrap { width: 100%; overflow: hidden; background: rgba(212, 175, 55, 0.05); border-bottom: 1px solid #d4af37; padding: 10px 0; margin-bottom: 30px; }
    .ticker-move { display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-size: 0.95rem; font-weight: bold; letter-spacing: 2px; }
    @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }
    
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; }
    .stTextArea > div > div > textarea { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ACCESO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    _, col_ce, _ = st.columns([1, 1.5, 1])
    with col_ce:
        emp = st.text_input("IDENTIFIQUE SU FIRMA:", key="e_fix_final")
        pw = st.text_input("MASTER KEY:", type="password", key="p_fix_final")
        if st.button("🔓 DESBLOQUEAR"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp.upper()
                st.session_state.auth = True; st.rerun()
            else: st.error("Datos requeridos.")
    st.stop()

# --- 4. INTERIOR TOTAL ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")

# TICKER GLOBAL (SIN PLÁTANOS)
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 LIVE MARKET | USDT/ARS: 1.515 ▲ | BTC/USD: 96.840 ▼ | ETH/USD: 2.720 ▲ | GOLD/OZ: 2.045 ▲ | 🛡️ AES-256 ACTIVE | 🌐 GLOBAL ENCRYPTION NODE: ACTIVE | TERMINAL: {emp} 🏛️</div></div>', unsafe_allow_html=True)

# MÉTRICAS CENTRADAS
c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$145M" if "GINEVRA" in emp else "$85M")
with c2: st.metric("YACHTS", "$25M" if "GINEVRA" in emp else "$12.5M")
with c3: st.metric("JETS", "$40M" if "GINEVRA" in emp else "$24M")

st.write("---")

# IA ADVISOR
st.subheader(f"🤖 ESTRATEGA IA PARA {emp}")
_, col_ia, _ = st.columns([0.5, 2, 0.5])
with col_ia:
    q = st.text_input("CONSULTA TÉCNICA:", key="q_ia_99")
    if q:
        with st.spinner("Analizando..."):
            time.sleep(1)
            st.markdown(f"<div class='gold-card'>🏛️ <b>IA ADVISOR:</b> Director de {emp}, análisis sobre '{q}' completado. Recomendación: MANTENER POSICIONES.</div>", unsafe_allow_html=True)

st.write("---")

# SCANNER DE ACTIVOS (RESTAURADO)
st.subheader("🧬 SCANNER DE ACTIVOS PATRIMONIALES")
_, col_sc, _ = st.columns([0.5, 2, 0.5])
with col_sc:
    activos = st.text_area("LISTA DE PROPIEDADES, AUTOS O YATES:", placeholder="Ej: 2 Ferraris, 1 Mansión en Nordelta...", key="sc_input_restore")
    if st.button("🧬 INICIAR ESCANEO QUÁNTICO"):
        if activos:
            with st.status("Escaneando...", expanded=True) as s:
                time.sleep(1); s.update(label="Escaneo Finalizado ✅", state="complete")
            st.markdown(f"<div class='gold-card'><h3>💎 VALUACIÓN DETECTADA</h3><p>Activos: <b>{activos}</b></p><h2 style='color:#d4af37;'>$42,500,000 USD</h2></div>", unsafe_allow_html=True)
        else: st.warning("⚠️ Ingrese activos.")

st.write("---")

# RELOJES
r1, r2, r3 = st.columns(3)
with r1: st.markdown("<div class='gold-card'>🗽 NY: 11:50 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 01:50 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 04:50 AM</div>", unsafe_allow_html=True)

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
