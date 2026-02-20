import streamlit as st
import pandas as pd
import time

# --- 1. BASE DE DATOS Y ESTADOS ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'solicitudes' not in st.session_state: st.session_state.solicitudes = []

# --- 2. DISEÑO DE ALTA GAMA (CSS) ---
st.set_page_config(page_title="LEGACY GOLD EMPIRE", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 6px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 2px solid #d4af37; width: 100%; height: 3em; font-weight: bold; }
    .ticker { background: #1a1a1a; color: #d4af37; padding: 10px; border-bottom: 2px solid #d4af37; font-weight: bold; text-align: center; }
    [data-testid='stMetricValue'] { color: #d4af37 !important; font-size: 3rem !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TICKER DE MERCADO ---
st.markdown("<div class='ticker'>🏦 MERCADO EN VIVO | USDT/ARS: 1.515 | BTC/USD: 96.850 | PROTOCOLO AES-256: ACTIVO</div>", unsafe_allow_html=True)

# --- 4. PANTALLA DE ENTRADA ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        region = st.selectbox("🌎 REGION:", ["🇦🇷 Argentina", "🇺🇸 USA"], key="reg_fix")
        st.markdown(f"<div class='gold-card'>🔑 LLAVE VIP: {'2.000.000 ARS' if 'Arg' in region else '12.000 USD'}</div>", unsafe_allow_html=True)
        pw = st.text_input("PASSWORD:", type="password", key="pw_fix")
        if st.button("DESBLOQUEAR BÓVEDA"):
            if pw == "LEGACY2026":
                st.session_state.auth = True
                st.session_state.reg_final = region
                st.rerun()
            else: st.error("DENEGADO")
        
        st.write("---")
        st.subheader("📩 ¿NO TIENE ACCESO?")
        with st.form("solicitud"):
            email = st.text_input("Email Corporativo:")
            nota = st.text_area("Mensaje al Founder:")
            if st.form_submit_button("SOLICITAR ACCESO VIP"):
                st.session_state.solicitudes.append({"Empresa": email, "Nota": nota, "Hora": time.strftime('%H:%M')})
                st.success("✅ Enviado a Dylan García.")
    st.stop()

# --- 5. INTERFAZ INTERNA (IMPERIO COMPLETO) ---
t = st.session_state.reg_final
st.markdown("<div style='background: #d4af37; color: black; padding: 10px; text-align: center; font-weight: bold;'>💎 ESTADO VIP: ACTIVO | BIENVENIDO DYLAN GARCÍA</div>", unsafe_allow_html=True)
st.title(f"🏛️ COMMAND CENTER - {t}")

# SIMULADOR
años = st.slider("PROYECCIÓN (AÑOS):", 1, 30, 10); ret = st.slider("RENTABILIDAD %:", 5, 50, 15)
fut_usd = 12450000 * ((1 + (ret/100))**años)
m1, m2 = st.columns(2)
m1.metric("FORTUNA USD", f"${fut_usd:,.0f}")
if "Arg" in t: m2.metric("FORTUNA ARS", f"${(fut_usd * 1515):,.0f}")

st.write("---")
# EXCHANGE
st.subheader("💹 MESA DE CAMBIO VIP (P2P)")
ex1, ex2 = st.columns(2)
with ex1:
    m_ars = st.number_input("Monto ARS:", min_value=1000000, value=5000000)
    st.write(f"Recibe: **{(m_ars/1515):,.2f} USDT**")
    if st.button("🚀 SOLICITAR COTIZACIÓN"):
        st.success("✅ Solicitud enviada a la mesa de operaciones.")
with ex2:
    m_btc = st.number_input("Monto BTC:", min_value=0.01, value=0.1)
    st.write(f"Recibe: **${(m_btc * 96850 * 1515):,.0f} ARS**")
    if st.button("🚀 LIQUIDAR BTC"):
        st.success("✅ Solicitud enviada.")

st.write("---")
# IA ADVISOR
st.subheader("🤖 ESTRATEGA IA: WALL STREET ADVISOR")
q = st.text_input("CONSULTA TÉCNICA:")
if q:
    with st.spinner('Analizando...'):
        time.sleep(1)
        st.write(f"🏛️ **IA:** Dylan García, para '{q}' la orden es MANTENER POSICIONES.")

st.write("---")
# RELOJES MUNDIALES
c_t1, c_t2, c_t3 = st.columns(3)
with c_t1: st.markdown("<div class='gold-card'>🗽 NY: 11:55 AM</div>", unsafe_allow_html=True)
with c_t2: st.markdown("<div class='gold-card'>🏢 BA: 13:55 PM</div>", unsafe_allow_html=True)
with c_t3: st.markdown("<div class='gold-card'>🏰 LN: 16:55 PM</div>", unsafe_allow_html=True)

st.markdown("<div style='text-align: center; color: #d4af37; padding: 20px;'>🔒 ENCRIPTACIÓN AES-256 | LEGACY VAULT © 2026 | BS. AS.</div>", unsafe_allow_html=True)

# MODO ADMIN
if st.sidebar.checkbox("🔓 MODO ADMIN"):
    if st.sidebar.text_input("CLAVE ESPÍA:", type="password") == "DYLAN777":
        if st.session_state.solicitudes: st.sidebar.table(pd.DataFrame(st.session_state.solicitudes))
        else: st.sidebar.info("Sin mensajes.")

if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False; st.rerun()
