import streamlit as st
import pandas as pd
import time
from datetime import datetime

# --- 1. LÓGICA DE ESTADOS ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'demo' not in st.session_state: st.session_state.demo = False
if 'start_time' not in st.session_state: st.session_state.start_time = None
if 'mensajes' not in st.session_state: st.session_state.mensajes = []

# --- 2. DISEÑO IMPERIAL (CSS) ---
st.set_page_config(page_title="LEGACY | COMMAND CENTER", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 6px solid #d4af37; padding: 25px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    [data-testid='stMetricValue'] { color: #d4af37 !important; font-size: 3rem !important; font-weight: bold; }
    .gold-box { border: 2px solid #d4af37; padding: 25px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    .ticker { background: #1a1a1a; color: #d4af37; padding: 10px; border-bottom: 2px solid #d4af37; font-weight: bold; text-align: center; font-size: 1.1rem; }
    .footer-vip { 
        margin-top: 50px; border-top: 1px solid #d4af37; padding-top: 30px; 
        text-align: center; color: #d4af37; font-size: 0.8rem; letter-spacing: 2px;
    }
    .clock-box { background: rgba(212, 175, 55, 0.1); padding: 10px; border-radius: 5px; margin: 5px; border: 1px solid #d4af37; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TICKER DE MERCADO ---
st.markdown("<div class='ticker'>🏦 MERCADO EN VIVO: USD/ARS: 1.510 (MEP) | BTC/USD: 96.450 | PROTOCOLO AES-256: ACTIVO</div>", unsafe_allow_html=True)

# --- 4. PANTALLA DE ENTRADA / CONTACTO ---
if not st.session_state.auth and not st.session_state.demo:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_iz, col_ce, col_de = st.columns([1, 1.5, 1])
    with col_ce:
        st.markdown("<div class='gold-box'>💎 ACCESO VIP: 2.000.000 ARS / 12K USD<br>Ingrese su llave o solicite una demo técnica.</div>", unsafe_allow_html=True)
        st.write("")
        if st.button("🔑 LLAVE MAESTRA"): st.session_state.auth = "login"; st.rerun()
        if st.button("🚀 AUDITORÍA DEMO (5 MIN)"): 
            st.session_state.demo = True; st.session_state.start_time = time.time(); st.rerun()
        st.write("---")
        st.subheader("📩 CONTACTO DIRECTO CON EL FOUNDER")
        with st.form("contacto_directo"):
            mail_cliente = st.text_input("Su Email Corporativo:")
            mensaje_cliente = st.text_area("Propuesta o Consulta:")
            if st.form_submit_button("ENVIAR AL FOUNDER"):
                if mail_cliente:
                    st.session_state.mensajes.append({"mail": mail_cliente, "nota": mensaje_cliente, "hora": time.strftime('%H:%M')})
                    st.success("✅ Mensaje encriptado y enviado a Dylan García.")
                else: st.warning("Ingrese su mail.")
    st.stop()

# --- 5. LOGIN SCANNER ---
if st.session_state.auth == "login":
    st.subheader("🔐 ESCANER DE IDENTIDAD VIP")
    pw = st.text_input("PASSWORD:", type="password")
    if st.button("DESBLOQUEAR BÓVEDA"):
        if pw == "LEGACY2026":
            with st.status("Analizando Encriptación AES-256...", expanded=True) as status:
                st.write("🧬 Verificando firma biométrica...")
                time.sleep(1)
                st.write("📡 Sincronizando con la red Legacy...")
                time.sleep(1)
                status.update(label="Acceso VIP Concedido", state="complete")
            st.session_state.auth = True; st.rerun()
    st.stop()

# --- 6. COMMAND CENTER (TODO EL CONTENIDO) ---
if st.session_state.auth == True:
    st.markdown("<div style='background: #d4af37; color: black; padding: 10px; text-align: center; font-weight: bold; border-radius: 5px;'>💎 ESTADO VIP: ACTIVO | BIENVENIDO DYLAN GARCÍA</div>", unsafe_allow_html=True)

st.title("🏛️ COMMAND CENTER LEGACY")

if st.session_state.demo:
    st.warning(f"⚠️ MODO DEMO ACTIVO: {int(300 - (time.time() - st.session_state.start_time))} segundos restantes")

# SIMULADOR
años = st.slider("PROYECCIÓN (AÑOS):", 1, 30, 10); ret = st.slider("RENTABILIDAD (%):", 5, 50, 15)
fut_usd = 12450000 * ((1 + (ret/100))**años)
m1, m2 = st.columns(2)
m1.metric("VALOR USD", f"${fut_usd:,.0f}"); m2.metric("VALOR ARS", f"${(fut_usd * 1510):,.0f}")

st.write("---")
st.subheader("📊 DISTRIBUCIÓN DE ACTIVOS ESTRATÉGICOS")
df = pd.DataFrame({"Activo": ["Real Estate", "Stocks", "Crypto", "Art"], "Valor": [45, 25, 20, 10]})
st.bar_chart(df.set_index("Activo"))

st.write("---")
st.subheader("🤖 ESTRATEGA IA: WALL STREET ADVISOR")
q = st.text_input("CONSULTA TÉCNICA:")
if q:
    with st.spinner('Analizando...'):
        time.sleep(1)
        st.write(f"🏛️ **IA:** Dylan García, para '{q}' el análisis sugiere **HOLD** y reinvertir dividendos.")

# --- 7. PIE DE PÁGINA IMPERIAL (RECOMPLETA EL ESPACIO VACÍO) ---
st.write("---")
st.markdown("<h3 style='font-size: 1rem;'>🌍 TIEMPO GLOBAL DE MERCADOS</h3>", unsafe_allow_html=True)
c_time1, c_time2, c_time3 = st.columns(3)
with c_time1: st.markdown("<div class='clock-box'>🗽 NEW YORK (NYSE)<br><b>10:41 AM</b></div>", unsafe_allow_html=True)
with c_time2: st.markdown("<div class='clock-box'>🏢 BS.AS. (BYMA)<br><b>12:41 PM</b></div>", unsafe_allow_html=True)
with c_time3: st.markdown("<div class='clock-box'>🏰 LONDON (LSE)<br><b>15:41 PM</b></div>", unsafe_allow_html=True)

st.markdown("""
    <div class='footer-vip'>
        🔒 ENCRIPTACIÓN DE GRADO MILITAR AES-256 ACTIVADA<br>
        PROPIEDAD EXCLUSIVA DE DYLAN GARCÍA | LEGACY VAULT © 2026<br>
        TODOS LOS DERECHOS RESERVADOS. PUERTO MADERO, BS. AS.
    </div>
    """, unsafe_allow_html=True)

# MODO ADMIN (SIDEBAR)
if st.sidebar.checkbox("🔓 MODO ADMIN"):
    if st.sidebar.text_input("CLAVE:", type="password") == "DYLAN777":
        st.sidebar.write("📬 Mails recibidos:")
        if st.session_state.mensajes: st.sidebar.table(pd.DataFrame(st.session_state.mensajes))
        else: st.sidebar.info("Esperando interesados...")

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.session_state.demo = False; st.rerun()
