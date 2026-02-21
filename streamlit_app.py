import streamlit as st
import time

# --- 1. MEMORIA Y SEGURIDAD ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg' not in st.session_state: st.session_state.reg = []

# LISTA BLANCA (Los 32 misiles)
VIP = ["EMAAR", "GINEVRA", "REMAX", "THE AGENCY", "CARSO", "LEGACY", "DYLAN", "ADMIN", "SOTHEBYS", "HINES"]

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; }
    .ticker-wrap { width: 100%; overflow: hidden; border-bottom: 1px solid #d4af37; padding: 10px 0; margin-bottom: 30px; }
    .ticker-move { display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-weight: bold; }
    @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; height: 3em; }
    .stTextArea > div > div > textarea { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ACCESO RESTRINGIDO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO AUTORIZADO</div>", unsafe_allow_html=True)
        emp_in = st.text_input("FIRMA / COMPANY:").strip().upper()
        pw_in = st.text_input("MASTER KEY:", type="password")
        if st.button("🔓 UNLOCK"):
            if pw_in == "LEGACY2026" and emp_in in VIP:
                st.session_state.emp_final = emp_in
                st.session_state.reg.append(f"🟢 {emp_in} - {time.strftime('%H:%M')}")
                st.session_state.auth = True; st.rerun()
            elif emp_in != "":
                st.error("ACCESO DENEGADO")
                st.session_state.reg.append(f"🔴 ERROR: {emp_in} - {time.strftime('%H:%M')}")
    st.stop()

# --- 4. INTERIOR TOTAL (EL IMPERIO) ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")

# TICKER
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 MARKET LIVE | BTC: 96,840 | GOLD: 2,045 | AES-256 ENCRYPTION ACTIVE | NODE: {emp} 🏛️</div></div>', unsafe_allow_html=True)

# MÉTRICAS
_, c1, c2, c3, _ = st.columns([0.1, 1, 1, 1, 0.1])
with c1: st.metric("REAL ESTATE", "$85,000,000")
with c2: st.metric("YACHTS", "$12,500,000")
with c3: st.metric("PRIVATE JETS", "$24,000,000")

st.write("---")
# IA ADVISOR
st.subheader(f"🤖 IA STRATEGIST FOR {emp}")
q = st.text_input("CONSULTA TÉCNICA:", key="q_ia")
if q:
    with st.spinner("Analizando..."):
        time.sleep(1)
        st.markdown(f"<div class='gold-card'>🏛️ <b>ADVISOR:</b> Análisis completado para {emp}. Estado: SOLVENTE.</div>", unsafe_allow_html=True)

st.write("---")
# SCANNER
st.subheader("🧬 SCANNER DE ACTIVOS PATRIMONIALES")
activos = st.text_area("LISTA DE ACTIVOS:", placeholder="Ej: 2 Ferraris...", key="sc_in")
if st.button("🧬 INICIAR ESCANEO"):
    if activos:
        with st.status("Escaneando...", expanded=True) as s:
            time.sleep(1.5); s.update(label="Finalizado ✅", state="complete")
        st.markdown(f"<div class='gold-card'><h3>💎 VALUACIÓN DETECTADA</h3><h2 style='color:#d4af37;'>$42,500,000 USD</h2></div>", unsafe_allow_html=True)

st.write("---")
# RELOJES
_, r1, r2, r3, _ = st.columns([0.1, 1, 1, 1, 0.1])
with r1: st.markdown("<div class='gold-card'>🗽 NY: 04:10 AM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 06:10 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 09:10 AM</div>", unsafe_allow_html=True)

# ADMIN
st.sidebar.markdown("### 🛡️ CONTROL")
if st.sidebar.text_input("PIN:", type="password") == "DYLAN777":
    for r in st.session_state.reg: st.sidebar.info(r)
if st.sidebar.button("🔒 EXIT"):
    st.session_state.auth = False; st.rerun()
