import streamlit as st
import time

# --- 1. LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'pago_step' not in st.session_state: st.session_state.pago_step = None

# --- 2. DISEÑO IMPERIAL (DORADO Y NEGRO TOTAL) ---
st.set_page_config(page_title="LEGACY GOLD EMPIRE", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; margin-bottom: 15px; }
    .ticker-wrap { width: 100%; overflow: hidden; background: rgba(212, 175, 55, 0.05); border-bottom: 1px solid #d4af37; padding: 10px 0; margin-bottom: 30px; }
    .ticker-move { display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-size: 0.95rem; font-weight: bold; letter-spacing: 2px; }
    @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; height: 3em; }
    .btn-pay { background-color: #d4af37; color: black; padding: 10px; border-radius: 8px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA (TODO RESTAURADO) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    
    with col_c:
        v_sel = st.selectbox("📂 SELECT VAULT:", ["ARGENTINA", "USA"], key="vault_final")
        st.markdown("<div class='gold-card'>💎 ADQUIRIR TERMINAL CORPORATIVA</div>", unsafe_allow_html=True)
        
        # LÓGICA DE PAGOS ACTIVA
        if st.session_state.pago_step is None:
            if v_sel == "ARGENTINA":
                if st.button("💳 MERCADO PAGO"): st.session_state.pago_step = "Mercado Pago"; st.rerun()
                if st.button("🏦 CUENTA DNI"): st.session_state.pago_step = "Cuenta DNI"; st.rerun()
            else:
                if st.button("🔵 PAYPAL / STRIPE"): st.session_state.pago_step = "PayPal"; st.rerun()
        else:
            m = st.session_state.pago_step
            st.info(f"Seleccionó: {m}. ¿Cómo desea recibir los datos?")
            u_ws = f"https://api.whatsapp.com{m}" # Cambiar número
            u_ml = f"mailto:dylanelpromaster25@://gmail.com{m}"
            st.markdown(f'<a href="{u_ws}" target="_blank" class="btn-pay" style="background:#25d366; color:white;">🟢 WHATSAPP</a>', unsafe_allow_html=True)
            st.markdown(f'<a href="{u_ml}" class="btn-pay">📩 EMAIL</a>', unsafe_allow_html=True)
            if st.button("⬅️ CAMBIAR MÉTODO"): st.session_state.pago_step = None; st.rerun()

        st.write("---")
        emp = st.text_input("IDENTIFIQUE SU FIRMA / COMPANY:", key="e_ent_99")
        pw = st.text_input("MASTER KEY:", type="password", key="p_ent_99")
        if st.button("🔓 DESBLOQUEAR BÓVEDA"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp.upper()
                st.session_state.auth = True; st.rerun()
            else: st.error("Identificación obligatoria.")
    st.stop()

# --- 4. INTERIOR (IMPERIO TOTAL) ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 LIVE MARKET | USDT/ARS: 1.515 ▲ | BTC/USD: 96.840 ▼ | GOLD/OZ: 2.045 ▲ | 🛡️ AES-256 ACTIVE | GLOBAL ENCRYPTION NODE: ACTIVE | TERMINAL: {emp} 🏛️</div></div>', unsafe_allow_html=True)

# MÉTRICAS
c1, c2, c3 = st.columns(3)
with c1: st.metric("REAL ESTATE", "$145M" if "GINEVRA" in emp else "$85M")
with c2: st.metric("YACHTS", "$25M" if "GINEVRA" in emp else "$12.5M")
with c3: st.metric("PRIVATE JETS", "$40M" if "GINEVRA" in emp else "$24M")

st.write("---")
# IA
st.subheader(f"🤖 ESTRATEGA IA PARA {emp}")
q = st.text_input("CONSULTA TÉCNICA:", key="q_ia_final")
if q:
    with st.spinner("Analizando..."):
        time.sleep(1)
        st.markdown(f"<div class='gold-card'>🏛️ <b>IA ADVISOR:</b> Director de {emp}, análisis sobre '{q}' completado. Recomendación: MANTENER POSICIONES.</div>", unsafe_allow_html=True)

st.write("---")
# SCANNER FERRARIS
st.subheader("🧬 SCANNER DE ACTIVOS")
activos = st.text_area("LISTA DE PROPIEDADES, AUTOS O YATES:", placeholder="Ej: 2 Ferraris...", key="sc_input_final")
if st.button("🧬 INICIAR ESCANEO QUÁNTICO"):
    if activos:
        with st.status("Escaneando...", expanded=True) as s:
            time.sleep(1); s.update(label="Escaneo Finalizado ✅", state="complete")
        st.markdown(f"<div class='gold-card'><h3>💎 VALUACIÓN DETECTADA</h3><h2 style='color:#d4af37;'>$42,500,000 USD</h2></div>", unsafe_allow_html=True)

st.write("---")
# RELOJES
r1, r2, r3 = st.columns(3)
with r1: st.markdown("<div class='gold-card'>🗽 NY: 11:50 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 01:50 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 04:50 AM</div>", unsafe_allow_html=True)

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.session_state.pago_step = None; st.rerun()
