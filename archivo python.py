import streamlit as st
import time

# --- 1. BASE DE DATOS DE EMPRESAS AUTORIZADAS (WHITELIST) ---
EMPRESAS_VIP = [
    "EMAAR", "DAMAC", "GINEVRA", "REMAX", "SOTHEBYS", "NEST SEEKERS", 
    "THE AGENCY", "HINES", "JLL", "CARSO", "ABILIA", "GICSA", "BE GRAND",
    "DYLAN777", "ADMIN", "LEGACY", "GUEST", "USER"
]

# --- 2. LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'registros' not in st.session_state: st.session_state.registros = []
if 'pago_step' not in st.session_state: st.session_state.pago_step = None

# --- 3. DISEÑO IMPERIAL (CENTRADO Y DORADO) ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; margin-bottom: 20px; }
    .ticker-wrap { width: 100%; overflow: hidden; background: rgba(212, 175, 55, 0.05); border-bottom: 1px solid #d4af37; padding: 10px 0; margin-bottom: 30px; }
    .ticker-move { display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-size: 0.95rem; font-weight: bold; letter-spacing: 2px; }
    @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; height: 3em; }
    .stTextArea > div > div > textarea { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. PANTALLA DE ACCESO BLINDADA ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        v_sel = st.selectbox("📂 SELECT REGION:", ["USA / GLOBAL", "ARGENTINA"], key="v_f")
        st.markdown("<div class='gold-card'>🔒 ACCESO RESTRINGIDO A NODOS AUTORIZADOS</div>", unsafe_allow_html=True)
        
        # PAGOS
        if st.session_state.pago_step is None:
            if st.button("💎 ACQUIRE VIP ACCESS"): st.session_state.pago_step = "PAY"; st.rerun()
        else:
            u_ws = f"https://api.whatsapp.com"
            st.markdown(f'<a href="{u_ws}" target="_blank" style="text-decoration:none;"><div style="background:#25d366; color:white; padding:10px; border-radius:10px; text-align:center; font-weight:bold;">🟢 CONTACT STRATEGIC DESK</div></a>', unsafe_allow_html=True)
            if st.button("⬅️ BACK"): st.session_state.pago_step = None; st.rerun()

        st.write("---")
        emp_input = st.text_input("FIRMA / COMPANY:", key="login_emp").upper()
        pw_input = st.text_input("MASTER KEY:", type="password", key="login_pw")
        
        if st.button("🔓 VALIDAR CREDENCIALES"):
            if pw_input == "LEGACY2026" and emp_input in EMPRESAS_VIP:
                st.session_state.emp_final = emp_input
                st.session_state.registros.append(f"🟢 {emp_input} - {time.strftime('%H:%M')}")
                st.session_state.auth = True; st.rerun()
            elif emp_input != "":
                st.error("🚫 FIRMA NO RECONOCIDA.")
                st.session_state.registros.append(f"🔴 FALLO: {emp_input} - {time.strftime('%H:%M')}")
    st.stop()

# --- 5. INTERIOR TOTAL (RESTAURADO) ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")

# TICKER
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 LIVE MARKET | BTC/USD: 96.840 ▼ | GOLD/OZ: 2.045 ▲ | 🛡️ AES-256 ACTIVE | GLOBAL NODE: {emp} 🏛️</div></div>', unsafe_allow_html=True)

# MÉTRICAS CENTRADAS
_, c1, c2, c3, _ = st.columns([0.1, 1, 1, 1, 0.1])
with c1: st.metric("REAL ESTATE", "$85M")
with c2: st.metric("YACHTS", "$12.5M")
with c3: st.metric("PRIVATE JETS", "$24M")

st.write("---")

# IA ADVISOR
st.subheader(f"🤖 ESTRATEGA IA PARA {emp}")
_, col_ia, _ = st.columns([0.5, 2, 0.5])
with col_ia:
    q = st.text_input("CONSULTA TÉCNICA:", key="q_ia")
    if q:
        with st.spinner("Analizando..."):
            time.sleep(1)
            st.markdown(f"<div class='gold-card'>🏛️ <b>IA ADVISOR:</b> Análisis completado. Estado: SOLVENTE.</div>", unsafe_allow_html=True)

st.write("---")

# SCANNER
st.subheader("🧬 SCANNER DE ACTIVOS")
_, col_sc, _ = st.columns([0.5, 2, 0.5])
with col_sc:
    activos = st.text_area("LISTA DE ACTIVOS:", placeholder="Ej: 2 Ferraris...", key="sc_in")
    if st.button("🧬 INICIAR ESCANEO"):
        if activos:
            with st.status("Escaneando...", expanded=True) as s:
                time.sleep(1); s.update(label="Escaneo Finalizado ✅", state="complete")
            st.markdown(f"<div class='gold-card'><h3>💎 VALUACIÓN DETECTADA</h3><h2 style='color:#d4af37;'>$42,500,000 USD</h2></div>", unsafe_allow_html=True)

st.write("---")

# RELOJES
_, r1, r2, r3, _ = st.columns([0.1, 1, 1, 1, 0.1])
with r1: st.markdown("<div class='gold-card'>🗽 NY: 11:50 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 05:40 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 08:40 AM</div>", unsafe_allow_html=True)

# SIDEBAR ADMIN
st.sidebar.markdown("### 🛡️ CONTROL")
if st.sidebar.text_input("ADMIN PIN:", type="password") == "DYLAN777":
    for r in st.session_state.registros: st.sidebar.info(r)

if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False
    st.rerun()
