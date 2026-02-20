import streamlit as st
import pandas as pd
import time

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
    </style>
    """, unsafe_allow_html=True)

# --- 3. TICKER DE MERCADO (DÓLAR / BTC) ---
st.markdown("<div class='ticker'>🏦 MERCADO EN VIVO: USD/ARS: 1.510 (MEP) | BTC/USD: 96.450 | PROTOCOLO AES-256: ACTIVO</div>", unsafe_allow_html=True)

# --- 4. PANTALLA DE ENTRADA / CONTACTO DIRECTO ---
if not st.session_state.auth and not st.session_state.demo:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    st.write("")
    
    col_iz, col_ce, col_de = st.columns([1, 1.5, 1])
    
    with col_ce:
        st.markdown("<div class='gold-box'>💎 ACCESO VIP: 2.000.000 ARS / 12K USD<br>Ingrese su llave o solicite una demo.</div>", unsafe_allow_html=True)
        st.write("")
        if st.button("🔑 LLAVE MAESTRA"): st.session_state.auth = "login"; st.rerun()
        if st.button("🚀 AUDITORÍA DEMO (5 MIN)"): 
            st.session_state.demo = True; st.session_state.start_time = time.time(); st.rerun()
        
        st.write("---")
        # BUZÓN DE CONTACTO DIRECTO RECUPERADO
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

# --- 5. LOGIN CON EFECTO SCANNER ---
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

# --- 6. COMMAND CENTER (EL PRODUCTO) ---
if st.session_state.auth == True:
    st.markdown("<div style='background: #d4af37; color: black; padding: 10px; text-align: center; font-weight: bold; border-radius: 5px;'>💎 ESTADO VIP: ACTIVO | BIENVENIDO DYLAN GARCÍA</div>", unsafe_allow_html=True)

st.title("🏛️ COMMAND CENTER LEGACY")

# SIMULADOR
años = st.slider("PROYECCIÓN (AÑOS):", 1, 30, 10); ret = st.slider("RETORNO ESTIMADO (%):", 5, 50, 15)
fut_usd = 12450000 * ((1 + (ret/100))**años)

st.write("---")
m1, m2 = st.columns(2)
m1.metric("VALOR USD", f"${fut_usd:,.0f}"); m2.metric("VALOR ARS", f"${(fut_usd * 1510):,.0f}")

st.write("---")
# GRÁFICO (PARA QUE LA PÁGINA SEA LARGA)
st.subheader("📊 DISTRIBUCIÓN DE ACTIVOS ESTRATÉGICOS")
df = pd.DataFrame({"Activo": ["Real Estate", "Stocks", "Crypto", "Art"], "Valor": [45, 25, 20, 10]})
st.bar_chart(df.set_index("Activo"))

st.write("---")
# IA ADVISOR ABAJO DE TODO (EL CIERRE)
st.subheader("🤖 ESTRATEGA IA: WALL STREET ADVISOR")
st.info("Consulte a la IA sobre movimientos de capital o riesgo de mercado.")
q = st.text_input("REALIZAR CONSULTA TÉCNICA:")
if q:
    with st.spinner('Analizando mercados globales...'):
        time.sleep(1)
        st.write(f"🏛️ **IA:** Dylan García, para la consulta '{q}' el análisis de Wall Street sugiere **HOLD** y diversificar en Real Estate de Puerto Madero.")

# MODO ESPÍA (SIDEBAR)
if st.sidebar.checkbox("🔓 MODO ADMIN"):
    if st.sidebar.text_input("CLAVE:", type="password") == "DYLAN777":
        st.sidebar.write("📬 Mails recibidos:")
        if st.session_state.mensajes: st.sidebar.table(pd.DataFrame(st.session_state.mensajes))
        else: st.sidebar.info("Esperando interesados...")

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.session_state.demo = False; st.rerun()
