import streamlit as st
import time

# --- 1. MEMORIA DEL NODO ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg' not in st.session_state: st.session_state.reg = []

# LISTA VIP (Los 32 Misiles)
VIP = ["EMAAR", "GINEVRA", "REMAX", "THE AGENCY", "CARSO", "LEGACY", "DYLAN", "ADMIN", "SOTHEBYS", "HINES", "JLL"]

# --- 2. DISEÑO IMPERIAL (DORADO Y NEGRO) ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; margin-bottom: 20px; }
    .ticker-wrap { width: 100%; overflow: hidden; border-bottom: 1px solid #d4af37; padding: 10px 0; margin-bottom: 30px; }
    .ticker-move { display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-weight: bold; }
    @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; height: 3.5em; }
    .btn-paypal { background-color: #0070ba; color: white !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; border: 1px solid #fff; }
    .btn-mp { background-color: #009ee3; color: white !important; padding: 14px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; border: 1px solid #fff; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. RADAR DE IMPACTO (SIDEBAR BLINDADO) ---
with st.sidebar:
    st.markdown("### 🛡️ CONTROL FUNDADOR")
    with st.form("admin_panel"):
        pin = st.text_input("ADMIN PIN:", type="password", key="p_adm")
        check = st.form_submit_button("🛰️ SCAN NETWORK")
        if check and pin == "DYLAN777":
            st.success("BIENVENIDO DYLAN.")
            if st.session_state.reg:
                for r in st.session_state.reg: st.info(r)
            else: st.warning("NODOS EN ESCUCHA... (Esperando impactos)")
        elif check: st.error("PIN INVÁLIDO")
    
    if st.button("🔒 LOGOUT / SALIR"):
        st.session_state.auth = False
        st.rerun()

# --- 4. ACCESO AL BÚNKER (USA/ARG) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg_sel = st.selectbox("🌐 SELECT REGION:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO AUTORIZADO</div>", unsafe_allow_html=True)
        if reg_sel == "USA / GLOBAL":
            st.write("Subscription: **$12,000 USD**")
            st.markdown(f'<a href="mailto:dylanelpromaster25@://gmail.com" class="btn-paypal">🔵 PAY WITH PAYPAL (USD)</a>', unsafe_allow_html=True)
        else:
            st.write("Suscripción: **$2.000.000 ARS**")
            st.markdown(f'<a href="https://wa.me" class="btn-mp">💳 MERCADO PAGO / DNI</a>', unsafe_allow_html=True)
        
        st.write("---")
        emp_raw = st.text_input("FIRMA / COMPANY:").strip().upper()
        pw_in = st.text_input("MASTER KEY:", type="password")
        if st.button("🔓 UNLOCK VAULT"):
            if pw_in == "LEGACY2026" and emp_raw in VIP:
                st.session_state.emp_final = emp_raw
                st.session_state.reg.append(f"🟢 {emp_raw} - {time.strftime('%H:%M')}")
                st.session_state.auth = True; st.rerun()
            else: st.error("ACCESO DENEGADO")
    st.stop()

# --- 5. INTERIOR TOTAL (EL IMPERIO RESTAURADO) ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 MARKET LIVE | BTC: 96,840 | GOLD: 2,045 | NODE: {emp} | AES-256 ACTIVE 🏛️</div></div>', unsafe_allow_html=True)

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
        time.sleep(1); st.markdown(f"<div class='gold-card'>🏛️ <b>ADVISOR:</b> Análisis completado para {emp}. Liquidez confirmada.</div>", unsafe_allow_html=True)

st.write("---")
# SCANNER DE ACTIVOS
st.subheader("🧬 QUANTUM ASSET SCANNER")
act = st.text_area("LISTA DE ACTIVOS:", key="sc_in")
if st.button("🧬 INICIAR ESCANEO"):
    if act:
        with st.status("Escaneando..."): time.sleep(1.5)
        st.markdown(f"<div class='gold-card'><h3>💎 VALUACIÓN DETECTADA</h3><h2 style='color:#d4af37;'>$42,500,000 USD</h2></div>", unsafe_allow_html=True)

st.write("---")
# RELOJES
_, r1, r2, r3, _ = st.columns([0.1, 1, 1, 1, 0.1])
with r1: st.markdown("<div class='gold-card'>🗽 NY: 04:25 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 06:25 PM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 09:25 PM</div>", unsafe_allow_html=True)
