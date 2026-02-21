import streamlit as st
import time

# --- 1. WHITELIST DE LOS 34 MISILES (Única forma de entrar) ---
VIP = ["EMAAR", "DAMAC", "NEOM", "GINEVRA", "REMAX", "SOTHEBYS", "THE AGENCY", "HINES", "JLL", "CARSO", "BARNES", "FEAU", "ZINGRAF", "GARCIN", "JUNOT", "KRETZ", "KNIGHT FRANK", "SAVILLS", "CBRE", "COLLIERS"]

# INICIALIZACIÓN DE MEMORIA
if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg' not in st.session_state: st.session_state.reg = []
if 'founder' not in st.session_state: st.session_state.founder = False

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000; border: 2px solid #d4af37; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 15px; border-radius: 10px; background: rgba(212, 175, 55, 0.05); text-align: center; margin-bottom: 10px; }
    .btn-pay { background-color: #1a1a1a; color: #fff !important; padding: 12px; border-radius: 8px; font-weight: bold; text-decoration: none; display: block; text-align: center; margin-bottom: 8px; border: 1px solid #d4af37; }
    div.stButton > button { background-color: #d4af37 !important; color: #000 !important; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOGIN BLINDADO (LA ÚNICA PUERTA) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg_sel = st.selectbox("🌐 REGION:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO</div>", unsafe_allow_html=True)
        if reg_sel == "USA / GLOBAL":
            st.markdown(f'<a href="mailto:dylanelpromaster25@://gmail.com" class="btn-pay">🔵 PAY WITH PAYPAL (EMAIL)</a>', unsafe_allow_html=True)
        else:
            st.markdown(f'<a href="mailto:dylanelpromaster25@://gmail.com" class="btn-pay">💳 MERCADO PAGO / DNI (EMAIL)</a>', unsafe_allow_html=True)
        
        st.write("---")
        emp = st.text_input("COMPANY:").strip().upper()
        pw = st.text_input("KEY:", type="password")
        
        if st.button("🔓 UNLOCK"):
            # ENTRADA EXCLUSIVA PARA DYLAN (ADMIN)
            if emp == "DYLAN777" and pw == "LEGACY2026":
                st.session_state.founder = True
                st.session_state.emp_final = "FOUNDER CONTROL"
                st.session_state.auth = True; st.rerun()
            # ENTRADA PARA CLIENTES (SOLO SI ESTÁN EN LA LISTA)
            elif pw == "LEGACY2026" and emp in VIP:
                st.session_state.emp_final = emp
                st.session_state.reg.append(f"🟢 {emp} - {time.strftime('%H:%M')}")
                st.session_state.auth = True; st.rerun()
            elif emp != "":
                st.error(f"🚫 ACCESO DENEGADO. FIRMA NO AUTORIZADA.")
                st.session_state.reg.append(f"🔴 ERROR: {emp} - {time.strftime('%H:%M')}")
    st.stop()

# --- 4. INTERIOR TOTAL (RESTAURADO) ---
st.title(f"🏛️ TERMINAL: {st.session_state.emp_final}")

# EL RADAR SOLO APARECE SI ENTRASTE COMO "DYLAN777"
if st.session_state.founder:
    with st.expander("🕵️‍♂️ RADAR DE IMPACTOS GLOBAL"):
        for r in st.session_state.reg: st.info(r)

st.metric("REAL ESTATE", "$85,000,000")

st.write("---")
st.subheader("🤖 IA STRATEGIC ADVISOR")
pregunta = st.text_input("CONSULTA A LA IA:")
if pregunta:
    with st.spinner("Procesando..."):
        time.sleep(1)
        st.success(f"Análisis completado para {st.session_state.emp_final}. Liquidez Óptima.")

st.write("---")
st.subheader("🧬 QUANTUM ASSET SCANNER")
activos = st.text_area("LISTA DE ACTIVOS:")
if st.button("🧬 INICIAR ESCANEO"):
    if activos:
        with st.spinner("Escaneando..."):
            time.sleep(1.5)
            st.markdown(f"<div class='gold-card'><h2>VALUACIÓN: $42,500,000 USD</h2></div>", unsafe_allow_html=True)

if st.sidebar.button("🔒 EXIT"):
    st.session_state.auth = False
    st.session_state.founder = False
    st.rerun()
