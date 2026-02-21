import streamlit as st
import time

# --- 1. LÓGICA DE MEMORIA (PERSISTENTE) ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'registros' not in st.session_state: st.session_state.registros = []
if 'pago_step' not in st.session_state: st.session_state.pago_step = None

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; margin-bottom: 20px; }
    .ticker-wrap { width: 100%; overflow: hidden; background: rgba(212, 175, 55, 0.05); border-bottom: 1px solid #d4af37; padding: 10px 0; margin-bottom: 30px; }
    .ticker-move { display: inline-block; white-space: nowrap; padding-left: 100%; animation: marquee 30s linear infinite; color: #d4af37; font-size: 0.95rem; font-weight: bold; letter-spacing: 2px; }
    @keyframes marquee { 0% { transform: translateX(0); } 100% { transform: translateX(-100%); } }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        v_sel = st.selectbox("📂 SELECT VAULT:", ["ARGENTINA", "USA"], key="v_99")
        st.markdown("<div class='gold-card'>💎 ADQUIRIR TERMINAL CORPORATIVA</div>", unsafe_allow_html=True)
        
        if st.session_state.pago_step is None:
            if v_sel == "ARGENTINA":
                if st.button("💳 MERCADO PAGO"): st.session_state.pago_step = "MP"; st.rerun()
                if st.button("🏦 CUENTA DNI"): st.session_state.pago_step = "DNI"; st.rerun()
            else:
                if st.button("🔵 PAYPAL"): st.session_state.pago_step = "USA"; st.rerun()
        else:
            m = st.session_state.pago_step
            st.info(f"Seleccionó: {m}")
            u_ws = f"https://api.whatsapp.com{m}" 
            st.markdown(f'<a href="{u_ws}" target="_blank" style="text-decoration:none;"><div style="background:#25d366; color:white; padding:10px; border-radius:10px; text-align:center; font-weight:bold; margin-bottom:10px;">🟢 WHATSAPP</div></a>', unsafe_allow_html=True)
            if st.button("⬅️ CAMBIAR MÉTODO"): st.session_state.pago_step = None; st.rerun()

        st.write("---")
        emp = st.text_input("FIRMA / COMPANY:", key="e_99")
        pw = st.text_input("MASTER KEY:", type="password", key="p_99")
        if st.button("🔓 DESBLOQUEAR"):
            if pw == "LEGACY2026" and emp:
                st.session_state.emp_final = emp.upper()
                st.session_state.registros.append(f"🏢 {emp.upper()} - {time.strftime('%H:%M')}")
                st.session_state.auth = True; st.rerun()
            else: st.error("Identificación obligatoria.")
    st.stop()

# --- 4. INTERIOR (COMMAND CENTER) ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")

# TICKER
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 LIVE MARKET | BTC/USD: 96.840 ▼ | GOLD/OZ: 2.045 ▲ | 🛡️ AES-256 ACTIVE | GLOBAL ENCRYPTION NODE: ACTIVE | TERMINAL: {emp} 🏛️</div></div>', unsafe_allow_html=True)

# MÉTRICAS
c1, c2, c3 = st.columns(3)
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

# --- PANEL ADMIN FORZADO (SIDEBAR) ---
st.sidebar.markdown("### 🛡️ CONTROL FUNDADOR")
admin_key = st.sidebar.text_input("PIN DE COMANDO:", type="password", key="admin_pin")

if admin_key == "DYLAN777":
    st.sidebar.success("ACCESO TOTAL ACTIVADO")
    st.sidebar.write("📬 ÚLTIMOS INGRESOS:")
    if st.session_state.registros:
        for r in st.session_state.registros:
            st.sidebar.info(r)
    else:
        st.sidebar.write("Sin visitas nuevas.")
elif admin_key != "":
    st.sidebar.error("PIN DENEGADO")

if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False
    st.session_state.pago_step = None
    st.rerun()
