import streamlit as st
import time

# --- 1. SEGURIDAD Y LISTA BLANCA ---
VIP = ["EMAAR", "GINEVRA", "REMAX", "THE AGENCY", "CARSO", "LEGACY", "DYLAN", "ADMIN", "SOTHEBYS", "HINES", "JLL"]

# INICIALIZACIÓN DE MEMORIA (FUNDAMENTAL)
if 'auth' not in st.session_state: st.session_state.auth = False
if 'reg' not in st.session_state: st.session_state.reg = []

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; margin-bottom: 20px; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; height: 3.5em; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    reg = st.selectbox("🌐 SELECT REGION / ELIJA REGIÓN:", ["USA / GLOBAL", "ARGENTINA"])
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO AUTORIZADO</div>", unsafe_allow_html=True)
        if reg == "USA / GLOBAL":
            st.write("Subscription: **$12,000 USD**")
            st.markdown(f'<a href="mailto:dylanelpromaster25@://gmail.com" style="text-decoration:none;"><div style="background:#0070ba; color:white; padding:12px; border-radius:10px; text-align:center; font-weight:bold; border:1px solid #fff;">🔵 PAY WITH PAYPAL (USD)</div></a>', unsafe_allow_html=True)
        else:
            st.write("Suscripción: **$2.000.000 ARS**")
            st.markdown(f'<a href="https://wa.me" style="text-decoration:none;"><div style="background:#009ee3; color:white; padding:12px; border-radius:10px; text-align:center; font-weight:bold; border:1px solid #fff;">🔵 MERCADO PAGO / DNI</div></a>', unsafe_allow_html=True)
        
        st.write("---")
        emp_raw = st.text_input("IDENTIFIQUE SU FIRMA / COMPANY:").strip().upper()
        pw_in = st.text_input("MASTER KEY:", type="password")
        if st.button("🔓 UNLOCK VAULT"):
            if pw_in == "LEGACY2026" and emp_raw in VIP:
                st.session_state.emp_final = emp_raw
                st.session_state.reg.append(f"🟢 {emp_raw} - {time.strftime('%H:%M')}")
                st.session_state.auth = True
                st.rerun()
            elif emp_raw != "":
                st.error("DENEGADO / DENIED")
                st.session_state.reg.append(f"🔴 ERROR: {emp_raw} - {time.strftime('%H:%M')}")
    st.stop()

# --- 4. INTERIOR TOTAL ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")
st.metric("REAL ESTATE", "$85,000,000")

# IA ADVISOR
st.subheader(f"🤖 IA STRATEGIST FOR {emp}")
q = st.text_input("CONSULTA TÉCNICA:", key="q_ia")
if q:
    with st.spinner("Analizando..."):
        time.sleep(1); st.markdown(f"<div class='gold-card'>🏛️ <b>ADVISOR:</b> Análisis completado para {emp}.</div>", unsafe_allow_html=True)

# --- 5. PANEL ADMIN (ESTO NO TE SACA) ---
st.sidebar.markdown("### 🛡️ CONTROL FUNDADOR")
# Usamos un key único para que no se pise con el login
pin_adm = st.sidebar.text_input("PIN ADMIN:", type="password", key="pin_final")

if pin_adm == "DYLAN777":
    st.sidebar.success("BIENVENIDO DYLAN.")
    if st.session_state.reg:
        for r in st.session_state.reg:
            st.sidebar.info(r)
    else:
        st.sidebar.warning("NODOS EN ESCUCHA... (Sin ingresos todavía)")

if st.sidebar.button("🔒 SALIR"):
    st.session_state.auth = False
    st.rerun()
