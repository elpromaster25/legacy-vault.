import streamlit as st
import time

# --- 1. LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'pago_step' not in st.session_state: st.session_state.pago_step = None
if 'registros' not in st.session_state: st.session_state.registros = []

# --- 2. DISEÑO IMPERIAL (CENTRADO Y DORADO) ---
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
    .btn-paypal { background-color: #0070ba; color: white; padding: 12px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; }
    .stTextArea > div > div > textarea { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA (MERCADO INTERNACIONAL) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        v_sel = st.selectbox("📂 SELECT REGION:", ["USA / GLOBAL", "ARGENTINA"], key="v_f")
        st.markdown("<div class='gold-card'>💎 ACQUIRE CORPORATE TERMINAL</div>", unsafe_allow_html=True)
        
        if st.session_state.pago_step is None:
            if v_sel == "USA / GLOBAL":
                if st.button("🔵 PAYPAL (DIRECT)"): st.session_state.pago_step = "PayPal"; st.rerun()
                st.markdown("<p style='font-size:0.8rem;'>Subscription: $12,000 USD</p>", unsafe_allow_html=True)
            else:
                if st.button("💳 MERCADO PAGO"): st.session_state.pago_step = "MP"; st.rerun()
                if st.button("🏦 CUENTA DNI"): st.session_state.pago_step = "DNI"; st.rerun()
                st.markdown("<p style='font-size:0.8rem;'>Suscripción: $2.000.000 ARS</p>", unsafe_allow_html=True)
        else:
            m = st.session_state.pago_step
            u_pp = f"mailto:dylanelpromaster25@://gmail.com."
            u_ws = f"https://api.whatsapp.com{m}" 
            if m == "PayPal":
                st.markdown(f'<a href="{u_pp}" class="btn-paypal">🔵 PROCEED TO PAYPAL</a>', unsafe_allow_html=True)
            else:
                st.markdown(f'<a href="{u_ws}" target="_blank" style="text-decoration:none;"><div style="background:#25d366; color:white; padding:10px; border-radius:10px; text-align:center; font-weight:bold; margin-bottom:10px;">🟢 WHATSAPP</div></a>', unsafe_allow_html=True)
            if st.button("⬅️ CHANGE METHOD"): st.session_state.pago_step = None; st.rerun()

        st.write("---")
        emp = st.text_input("FIRMA / COMPANY:", key="e_ent")
        pw = st.text_input("MASTER KEY:", type="password", key="p_ent")
        if st.button("🔓 UNLOCK VAULT"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp.upper()
                st.session_state.registros.append(f"🏢 {emp.upper()} - {time.strftime('%H:%M')}")
                st.session_state.auth = True; st.rerun()
            else: st.error("Access Denied.")
    st.stop()

# --- 4. INTERIOR TOTAL (RESTAURADO) ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 LIVE MARKET | BTC/USD: 96.840 ▼ | GOLD/OZ: 2.045 ▲ | 🛡️ AES-256 ACTIVE | GLOBAL ENCRYPTION NODE: ACTIVE | TERMINAL: {emp} 🏛️</div></div>', unsafe_allow_html=True)

# MÉTRICAS CENTRADAS
_, c1, c2, c3, _ = st.columns([0.1, 1, 1, 1, 0.1])
with c1: st.metric("REAL ESTATE", "$85M")
with c2: st.metric("YACHTS", "$12.5M")
with c3: st.metric("PRIVATE JETS", "$24M")

st.write("---")
# IA ADVISOR
st.subheader(f"🤖 ESTRATEGA IA PARA {emp}")
q = st.text_input("CONSULTA TÉCNICA:", key="q_ia")
if q:
    with st.spinner("Analizando..."):
        time.sleep(1)
        st.markdown(f"<div class='gold-card'>🏛️ <b>IA ADVISOR:</b> Director de {emp}, análisis completado.</div>", unsafe_allow_html=True)

st.write("---")
# SCANNER DE ACTIVOS
st.subheader("🧬 SCANNER DE ACTIVOS")
activos = st.text_area("LISTA DE PROPIEDADES, AUTOS O YATES:", placeholder="Ej: 2 Ferraris...", key="sc_in")
if st.button("🧬 INICIAR ESCANEO"):
    if activos:
        with st.status("Escaneando...", expanded=True) as s:
            time.sleep(1); s.update(label="Escaneo Finalizado ✅", state="complete")
        st.markdown(f"<div class='gold-card'><h3>💎 VALUACIÓN DETECTADA</h3><h2 style='color:#d4af37;'>$42,500,000 USD</h2></div>", unsafe_allow_html=True)

st.write("---")
# RELOJES
_, r1, r2, r3, _ = st.columns([0.1, 1, 1, 1, 0.1])
with r1: st.markdown("<div class='gold-card'>🗽 NY: 11:50 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 03:10 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 06:10 AM</div>", unsafe_allow_html=True)

# --- PANEL ADMIN (SIDEBAR) ---
st.sidebar.markdown("### 🛡️ CONTROL FUNDADOR")
pin_adm = st.sidebar.text_input("PIN:", type="password", key="adm_pin")
if pin_adm == "DYLAN777":
    st.sidebar.success("BIENVENIDO DYLAN.")
    for r in st.session_state.registros: st.sidebar.info(r)

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.session_state.pago_step = None; st.rerun()
