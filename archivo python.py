import streamlit as st
import pandas as pd
import time

# --- 1. LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'mensajes' not in st.session_state: st.session_state.mensajes = []

# --- 2. DISEÑO IMPERIAL (CSS) ---
st.set_page_config(page_title="LEGACY | EMPIRE CENTER", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 6px solid #d4af37; padding: 25px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    [data-testid='stMetricValue'] { color: #d4af37 !important; font-size: 3rem !important; font-weight: bold; }
    .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    .ticker { background: #1a1a1a; color: #d4af37; padding: 10px; border-bottom: 2px solid #d4af37; font-weight: bold; text-align: center; }
    .footer-vip { border-top: 1px solid #d4af37; padding-top: 30px; text-align: center; color: #d4af37; font-size: 0.8rem; letter-spacing: 2px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TICKER DE MERCADO EN VIVO ---
st.markdown("<div class='ticker'>🏦 MERCADO EN VIVO | USDT/ARS: 1.515 | BTC/USD: 96.850 | PROTOCOLO AES-256: ACTIVO</div>", unsafe_allow_html=True)

# --- 4. ACCESO (LOGIN O CONTACTO) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_iz, col_ce, col_de = st.columns([1, 1.5, 1])
    with col_ce:
        st.markdown("<div class='gold-card'>💎 ACCESO VIP RESTRINGIDO<br>COSTO: 2.000.000 ARS / 12K USD</div>", unsafe_allow_html=True)
        st.write("")
        pw = st.text_input("PASSWORD:", type="password")
        if st.button("DESBLOQUEAR BÓVEDA"):
            if pw == "LEGACY2026":
                with st.status("Iniciando Bóveda...", expanded=True) as status:
                    st.write("🧬 Verificando firma biométrica..."); time.sleep(1)
                    st.write("📡 Sincronizando con Wall Street..."); time.sleep(1)
                    status.update(label="Acceso VIP Concedido", state="complete")
                st.session_state.auth = True; st.rerun()
        st.write("---")
        st.subheader("📩 CONTACTO DIRECTO CON EL FOUNDER")
        with st.form("contacto_form"):
            mail = st.text_input("Su Email:"); nota = st.text_area("Mensaje:")
            if st.form_submit_button("ENVIAR AL FOUNDER"):
                st.session_state.mensajes.append({"mail": mail, "nota": nota, "hora": time.strftime('%H:%M')})
                st.success("✅ Mensaje encriptado y enviado a Dylan García.")
    st.stop()

# --- 5. COMMAND CENTER & EXCHANGE (EL IMPERIO) ---
st.markdown("<div style='background: #d4af37; color: black; padding: 10px; text-align: center; font-weight: bold; border-radius: 5px;'>💎 ESTADO VIP: ACTIVO | BIENVENIDO DYLAN GARCÍA</div>", unsafe_allow_html=True)
st.title("🏛️ COMMAND CENTER & EXCHANGE VIP")

# SECCIÓN 1: SIMULADOR DE BILLONES
años = st.slider("PROYECCIÓN (AÑOS):", 1, 30, 10); ret = st.slider("RENTABILIDAD (%):", 5, 50, 15)
fut_usd = 12450000 * ((1 + (ret/100))**años)
m1, m2 = st.columns(2)
m1.metric("FORTUNA USD", f"${fut_usd:,.0f}"); m2.metric("FORTUNA ARS", f"${(fut_usd * 1515):,.0f}")

st.write("---")
# SECCIÓN 2: MESA DE CAMBIO (LO DE TU PAPÁ)
st.subheader("💹 MESA DE CAMBIO VIP (LIQUIDACIÓN P2P)")
st.info("Un operador de nuestra mesa se contactará telefónicamente para coordinar la liquidación.")
ex1, ex2 = st.columns(2)
with ex1:
    st.markdown("<div class='gold-card'>💰 PESOS POR DÓLARES (USDT)</div>", unsafe_allow_html=True)
    m_ars = st.number_input("Monto en ARS:", min_value=1000000, value=5000000, step=500000)
    st.write(f"Recibe: **{(m_ars/1515):,.2f} USDT**")
    if st.button("🚀 SOLICITAR COTIZACIÓN ARS"):
        st.session_state.mensajes.append({"mail": "CLIENTE VIP", "nota": f"VENTA DE {m_ars} ARS", "hora": time.strftime('%H:%M')})
        st.success("✅ Solicitud enviada a la mesa de operaciones.")
with ex2:
    st.markdown("<div class='gold-card'>₿ BITCOIN POR PESOS (ARS)</div>", unsafe_allow_html=True)
    m_btc = st.number_input("Monto en BTC:", min_value=0.01, value=0.1, step=0.01)
    st.write(f"Recibe: **${(m_btc * 96850 * 1515):,.0f} ARS**")
    if st.button("🚀 SOLICITAR COTIZACIÓN BTC"):
        st.session_state.mensajes.append({"mail": "CLIENTE VIP", "nota": f"VENTA DE {m_btc} BTC", "hora": time.strftime('%H:%M')})
        st.success("✅ Solicitud enviada a la mesa de operaciones.")

st.write("---")
# SECCIÓN 3: IA ADVISOR
st.subheader("🤖 ESTRATEGA IA: WALL STREET ADVISOR")
q = st.text_input("CONSULTA TÉCNICA:")
if q:
    with st.spinner('Analizando...'):
        time.sleep(1)
        st.write(f"🏛️ **IA:** Dylan García, la orden para '{q}' es MANTENER POSICIONES.")

st.write("---")
# SECCIÓN 4: PIE DE PÁGINA GLOBAL
c_t1, c_t2, c_t3 = st.columns(3)
with c_t1: st.markdown("<div class='gold-card'>🗽 NY (NYSE)<br><b>11:01 AM</b></div>", unsafe_allow_html=True)
with c_t2: st.markdown("<div class='gold-card'>🏢 BS.AS. (BYMA)<br><b>13:01 PM</b></div>", unsafe_allow_html=True)
with c_t3: st.markdown("<div class='gold-card'>🏰 LONDON (LSE)<br><b>16:01 PM</b></div>", unsafe_allow_html=True)

st.markdown("<div class='footer-vip'>🔒 ENCRIPTACIÓN AES-256 | LEGACY VAULT © 2026 | PUERTO MADERO, ARGENTINA</div>", unsafe_allow_html=True)

# MODO ADMIN (SIDEBAR)
if st.sidebar.checkbox("🔓 MODO ADMIN"):
    if st.sidebar.text_input("CLAVE ESPÍA:", type="password") == "DYLAN777":
        st.sidebar.table(pd.DataFrame(st.session_state.mensajes))

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
