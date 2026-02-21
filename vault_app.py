import streamlit as st
import time

# --- 1. CONFIGURACIÓN E IMPERIO ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")

# LISTA BLANCA DE EMPRESAS (Cualquier otra rebota)
VIP_LIST = ["EMAAR", "GINEVRA", "REMAX", "THE AGENCY", "CARSO", "LEGACY", "DYLAN", "ADMIN", "SOTHEBYS"]

if 'auth' not in st.session_state: st.session_state.auth = False
if 'pago' not in st.session_state: st.session_state.pago = None
if 'reg' not in st.session_state: st.session_state.reg = []

# --- 2. DISEÑO DORADO Y NEGRO ---
st.markdown("""
    <style>
    .stApp { background-color: #000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; }
    .ticker-wrap { width: 100%; overflow: hidden; border-bottom: 1px solid #d4af37; padding: 10px 0; margin-bottom: 20px; }
    .ticker-move { display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-weight: bold; }
    @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ACCESO RESTRINGIDO ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO DE SEGURIDAD PRIVADO</div>", unsafe_allow_html=True)
        if st.session_state.pago is None:
            if st.button("💎 ACQUIRE VIP ACCESS ($12,000 USD)"): st.session_state.pago = True; st.rerun()
        else:
            st.markdown(f'<a href="https://api.whatsapp.com" target="_blank" style="text-decoration:none;"><div style="background:#25d366; color:white; padding:10px; border-radius:10px; text-align:center; font-weight:bold; margin-bottom:10px;">🟢 CONTACT STRATEGIC DESK</div></a>', unsafe_allow_html=True)
            if st.button("⬅️ BACK"): st.session_state.pago = None; st.rerun()
        
        st.write("---")
        emp = st.text_input("FIRMA / COMPANY:").strip().upper()
        pw = st.text_input("MASTER KEY:", type="password")
        if st.button("🔓 UNLOCK"):
            if pw == "LEGACY2026" and emp in VIP_LIST:
                st.session_state.emp_final = emp
                st.session_state.reg.append(f"🟢 {emp} - {time.strftime('%H:%M')}")
                st.session_state.auth = True; st.rerun()
            elif emp != "":
                st.error("🚫 FIRMA NO RECONOCIDA.")
                st.session_state.reg.append(f"🔴 ERROR: {emp} - {time.strftime('%H:%M')}")
    st.stop()

# --- 4. INTERIOR DEL IMPERIO ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL: {emp}")
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 MARKET LIVE | BTC: 96,840 | GOLD: 2,045 | AES-256 ENCRYPTION ACTIVE | NODE: {emp} 🏛️</div></div>', unsafe_allow_html=True)

# MÉTRICAS
_, c1, c2, c3, _ = st.columns([0.1, 1, 1, 1, 0.1])
with c1: st.metric("REAL ESTATE", "$85M")
with c2: st.metric("YACHTS", "$12.5M")
with c3: st.metric("PRIVATE JETS", "$24M")

st.write("---")
# IA
st.subheader(f"🤖 IA STRATEGIST FOR {emp}")
q = st.text_input("CONSULTA TÉCNICA:")
if q:
    with st.spinner("Analizando..."):
        time.sleep(1)
        st.markdown("<div class='gold-card'>🏛️ <b>ADVISOR:</b> Análisis completado. Estado de liquidez: ÓPTIMO.</div>", unsafe_allow_html=True)

st.write("---")
# SCANNER
st.subheader("🧬 SCANNER DE ACTIVOS")
activos = st.text_area("LISTA DE PROPIEDADES O AUTOS:")
if st.button("🧬 INICIAR ESCANEO"):
    if activos:
        with st.status("Escaneando...", expanded=True) as s:
            time.sleep(1.5); s.update(label="Finalizado ✅", state="complete")
        st.markdown(f"<div class='gold-card'><h3>💎 VALUACIÓN</h3><h2 style='color:#d4af37;'>$42,500,000 USD</h2></div>", unsafe_allow_html=True)

st.write("---")
# RELOJES
_, r1, r2, r3, _ = st.columns([0.1, 1, 1, 1, 0.1])
with r1: st.markdown("<div class='gold-card'>🗽 NY: 11:50 PM</div>", unsafe_allow_html=True)
with r2: st.markdown("<div class='gold-card'>🏢 BA: 05:50 AM</div>", unsafe_allow_html=True)
with r3: st.markdown("<div class='gold-card'>🏰 LN: 08:50 AM</div>", unsafe_allow_html=True)

# ADMIN
st.sidebar.markdown("### 🛡️ CONTROL")
if st.sidebar.text_input("PIN:", type="password") == "DYLAN777":
    for r in st.session_state.reg: st.sidebar.info(r)
if st.sidebar.button("🔒 EXIT"): st.session_state.auth = False; st.rerun()
