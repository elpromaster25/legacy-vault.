import streamlit as st
import pandas as pd
import time

# --- 1. LÓGICA DE ESTADOS Y DEMO ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'demo' not in st.session_state: st.session_state.demo = False
if 'start_time' not in st.session_state: st.session_state.start_time = None
if 'solicitudes' not in st.session_state: st.session_state.solicitudes = []

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY GOLD EMPIRE", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000000; border: 6px solid #d4af37; padding: 20px; }
    h1, h2, h3 { color: #d4af37 !important; text-align: center; font-family: 'serif'; }
    .gold-card { border: 2px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; color: #d4af37; }
    div.stButton > button { background-color: #1a1a1a; color: #d4af37; border: 2px solid #d4af37; width: 100%; height: 3em; font-weight: bold; }
    .ticker { background: #1a1a1a; color: #d4af37; padding: 10px; border-bottom: 2px solid #d4af37; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TICKER DE MERCADO ---
st.markdown("<div class='ticker'>🏦 MERCADO EN VIVO | USDT/ARS: 1.515 | BTC/USD: 96.850 | PROTOCOLO AES-256: ACTIVO</div>", unsafe_allow_html=True)

# --- 4. PANTALLA DE ENTRADA (ESTRATEGIA DEMO) ---
if not st.session_state.auth and not st.session_state.demo:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        region = st.selectbox("🌎 ELIJA SU REGIÓN / REGION:", ["🇦🇷 Argentina", "🇺🇸 USA"])
        st.write("---")
        
        # OPCIÓN 1: LA DEMO (EL ANZUELO)
        st.markdown("<div class='gold-card'>🚀 AUDITORÍA TÉCNICA GRATUITA<br>Acceso completo por 5 minutos</div>", unsafe_allow_html=True)
        if st.button("🚀 INICIAR DEMO GRATIS"):
            st.session_state.demo = True
            st.session_state.start_time = time.time()
            st.session_state.reg_final = region
            st.rerun()
        
        st.write("---")
        # OPCIÓN 2: LA LLAVE (EL CIERRE)
        st.markdown(f"<div class='gold-card'>🔑 LLAVE MAESTRA PERMANENTE<br>Suscripción VIP Activada</div>", unsafe_allow_html=True)
        pw = st.text_input("INGRESE SU PASSWORD:", type="password")
        if st.button("🔓 DESBLOQUEAR ACCESO TOTAL"):
            if pw == "LEGACY2026":
                st.session_state.auth = True
                st.session_state.reg_final = region
                st.rerun()
            else: st.error("DENEGADO / DENIED")
            
        st.write("---")
        # FORMULARIO DE CONTACTO
        with st.expander("📩 ¿NECESITA UNA LLAVE O SOPORTE?"):
            with st.form("solicitud"):
                email = st.text_input("Email Corporativo:")
                nota = st.text_area("Mensaje:")
                if st.form_submit_button("SOLICITAR ACCESO VIP"):
                    st.session_state.solicitudes.append({"Empresa": email, "Nota": nota, "Hora": time.strftime('%H:%M')})
                    st.success("✅ Enviado.")
    st.stop()

# --- 5. CONTROL DE TIEMPO DEMO ---
if st.session_state.demo and not st.session_state.auth:
    elapsed = time.time() - st.session_state.start_time
    if elapsed > 300: # 5 minutos
        st.title("⌛ TIEMPO DE DEMO EXPIRADO")
        st.markdown(f"<div class='gold-card'>PARA CONTINUAR OPERANDO ADQUIERA SU LLAVE MAESTRA<br>COSTO: {'2.000.000 ARS' if 'Arg' in st.session_state.reg_final else '12.000 USD'} / MES</div>", unsafe_allow_html=True)
        if st.button("⬅️ VOLVER AL INICIO"):
            st.session_state.demo = False
            st.rerun()
        st.stop()

# --- 6. INTERFAZ INTERNA (PODER TOTAL) ---
t = st.session_state.reg_final
st.markdown("<div style='background: #d4af37; color: black; padding: 10px; text-align: center; font-weight: bold;'>💎 ESTADO: ACCESO VIP | BIENVENIDO DYLAN GARCÍA</div>", unsafe_allow_html=True)
if st.session_state.demo:
    st.warning(f"⚠️ MODO DEMO: Quedan {int(300 - (time.time() - st.session_state.start_time))} segundos.")

st.title(f"🏛️ COMMAND CENTER - {t}")

# SIMULADOR
años = st.slider("PROYECCIÓN:", 1, 30, 10); ret = st.slider("RETORNO %:", 5, 50, 15)
fut_usd = 12450000 * ((1 + (ret/100))**años)
m1, m2 = st.columns(2)
m1.metric("USD VALUE", f"${fut_usd:,.0f}")
if "Arg" in t: m2.metric("ARS VALUE", f"${(fut_usd * 1515):,.0f}")

st.write("---")
# EXCHANGE
st.subheader("💹 MESA DE CAMBIO VIP (P2P)")
st.write(f"Solicite liquidación enviando un mail a: **dylanelpromaster25@gmail.com**")
ex1, ex2 = st.columns(2)
with ex1:
    m_ars = st.number_input("ARS:", min_value=1000000, value=2000000)
    if st.button("🚀 COTIZAR ARS"): st.success("Solicitud enviada.")
with ex2:
    m_btc = st.number_input("BTC:", min_value=0.01, value=0.1)
    if st.button("🚀 LIQUIDAR BTC"): st.success("Solicitud enviada.")

st.write("---")
# IA
st.subheader("🤖 ESTRATEGA IA")
q = st.text_input("CONSULTA TÉCNICA:")
if q: st.write("🏛️ **IA:** Dylan García, la orden es MANTENER POSICIONES.")

st.write("---")
# PIE DE PÁGINA
c_t1, c_t2, c_t3 = st.columns(3)
with c_t1: st.markdown("<div class='gold-card'>🗽 NY: 11:57 AM</div>", unsafe_allow_html=True)
with c_t2: st.markdown("<div class='gold-card'>🏢 BA: 13:57 PM</div>", unsafe_allow_html=True)
with c_t3: st.markdown("<div class='gold-card'>🏰 LN: 16:57 PM</div>", unsafe_allow_html=True)

# MODO ADMIN
if st.sidebar.checkbox("🔓 ADMIN"):
    if st.sidebar.text_input("CLAVE:", type="password") == "DYLAN777":
        st.sidebar.table(pd.DataFrame(st.session_state.solicitudes))

if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False
    st.session_state.demo = False
    st.rerun()
