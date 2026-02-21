import streamlit as st
import time

# --- 1. BASE DE DATOS DE EMPRESAS AUTORIZADAS (WHITELIST) ---
# Agregamos los 32 misiles que mandamos
EMPRESAS_VIP = [
    "EMAAR", "DAMAC", "GINEVRA", "REMAX", "SOTHEBYS", "NEST SEEKERS", 
    "THE AGENCY", "HINES", "JLL", "CARSO", "ABILIA", "GICSA", "BE GRAND",
    "DYLAN777", "ADMIN", "LEGACY" # Tus claves de acceso
]

# --- 2. LÓGICA DE SESIÓN ---
if 'auth' not in st.session_state: st.session_state.auth = False
if 'registros' not in st.session_state: st.session_state.registros = []

# --- 3. DISEÑO IMPERIAL (MODO OSCURO PARA EL OJO ROJO) ---
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

# --- 4. PANTALLA DE ACCESO BLINDADA ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 ACCESO RESTRINGIDO A NODOS AUTORIZADOS</div>", unsafe_allow_html=True)
        emp_input = st.text_input("IDENTIFIQUE SU FIRMA / COMPANY:", key="login_emp").upper()
        pw_input = st.text_input("MASTER KEY:", type="password", key="login_pw")
        
        if st.button("🔓 VALIDAR CREDENCIALES"):
            # AHORA VALIDAMOS QUE ESTÉ EN LA LISTA
            if pw_input == "LEGACY2026" and emp_input in EMPRESAS_VIP:
                st.session_state.emp_final = emp_input
                st.session_state.registros.append(f"🟢 ACCESO: {emp_input} - {time.strftime('%H:%M')}")
                st.session_state.auth = True
                st.success("AUTORIZADO. Entrando al Nodo...")
                time.sleep(1); st.rerun()
            elif emp_input not in EMPRESAS_VIP and emp_input != "":
                st.error("🚫 FIRMA NO RECONOCIDA. Acceso denegado por el Nodo Central.")
                st.session_state.registros.append(f"🔴 FALLO: {emp_input} - {time.strftime('%H:%M')}")
            else:
                st.warning("Ingrese credenciales válidas.")
    st.stop()

# --- 5. INTERIOR (SOLO SI PASÓ EL FILTRO) ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")
st.markdown(f'<div class="ticker-wrap"><div class="ticker-move">🏦 LIVE MARKET | BTC/USD: 96.840 ▼ | GOLD/OZ: 2.045 ▲ | 🛡️ AES-256 ACTIVE | GLOBAL NODE: {emp} 🏛️</div></div>', unsafe_allow_html=True)

# PANEL ADMIN (SIDEBAR)
st.sidebar.markdown("### 🛡️ RADAR DE SEGURIDAD")
if st.sidebar.text_input("PIN ADMIN:", type="password") == "DYLAN777":
    st.sidebar.success("BIENVENIDO FOUNDER.")
    for r in st.session_state.registros: st.sidebar.info(r)

if st.sidebar.button("🔒 SALIR"): st.session_state.auth = False; st.rerun()
