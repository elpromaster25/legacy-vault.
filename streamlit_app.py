import streamlit as st
import time

# --- 1. SEGURIDAD Y LISTA BLANCA ---
VIP = ["EMAAR", "GINEVRA", "REMAX", "THE AGENCY", "CARSO", "LEGACY", "DYLAN", "ADMIN", "SOTHEBYS", "HINES"]

if 'auth' not in st.session_state: st.session_state.auth = False
if 'pago' not in st.session_state: st.session_state.pago = None

# --- 2. DISEÑO IMPERIAL ---
st.set_page_config(page_title="LEGACY GOLD VAULT", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000; border: 5px solid #d4af37; padding: 20px; }
    h1, h2, h3, p, label, .stMetric { color: #d4af37 !important; text-align: center !important; }
    .gold-card { border: 1px solid #d4af37; padding: 20px; border-radius: 15px; background: rgba(212, 175, 55, 0.05); text-align: center; }
    div.stButton > button { background-color: #1a1a1a !important; color: #d4af37 !important; border: 1px solid #d4af37 !important; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. PANTALLA DE ENTRADA (SELECTOR Y NOTIFICACIÓN) ---
if not st.session_state.auth:
    st.title("🏛️ LEGACY QUANTUM VAULT")
    _, col_c, _ = st.columns([1, 1.5, 1])
    with col_c:
        # SELECTOR DE REGIÓN
        region = st.selectbox("🌐 SELECT YOUR REGION / ELIJA SU REGIÓN:", ["USA / GLOBAL", "ARGENTINA"])
        
        st.markdown("<div class='gold-card'>🔒 NODO PRIVADO AUTORIZADO</div>", unsafe_allow_html=True)
        
        # PRECIOS SEGÚN REGIÓN
        if region == "USA / GLOBAL":
            st.write("Subscription: **$12,000 USD**")
            u_mail = "mailto:dylanelpromaster25@://gmail.com."
            st.markdown(f'<a href="{u_mail}" target="_blank" style="text-decoration:none;"><div style="background:#d4af37; color:black; padding:10px; border-radius:10px; text-align:center; font-weight:bold; margin-bottom:10px;">📩 REQUEST VIP ACCESS (EMAIL)</div></a>', unsafe_allow_html=True)
        else:
            st.write("Suscripción: **$2.000.000 ARS**")
            u_mp = "https://api.whatsapp.com"
            st.markdown(f'<a href="{u_mp}" target="_blank" style="text-decoration:none;"><div style="background:#009ee3; color:white; padding:10px; border-radius:10px; text-align:center; font-weight:bold; margin-bottom:10px;">💳 MERCADO PAGO / CUENTA DNI</div></a>', unsafe_allow_html=True)

        st.write("---")
        # LOGIN
        emp = st.text_input("IDENTIFIQUE SU FIRMA / COMPANY:").strip().upper()
        pw = st.text_input("MASTER KEY:", type="password")
        if st.button("🔓 UNLOCK VAULT"):
            if pw == "LEGACY2026" and emp in VIP:
                st.session_state.emp_final = emp
                st.session_state.auth = True; st.rerun()
            else: st.error("ACCESS DENIED / ACCESO DENEGADO")
    st.stop()

# --- 4. INTERIOR (EL IMPERIO) ---
emp = st.session_state.emp_final
st.title(f"🏛️ TERMINAL EXCLUSIVA: {emp}")
st.metric("REAL ESTATE ASSETS", "$85,000,000")

# IA Y SCANNER
st.subheader("🤖 IA STRATEGIC ADVISOR")
st.info(f"Análisis activo para la firma **{emp}**. Portafolio en estado SOLVENTE.")

st.write("---")
st.subheader("🧬 QUANTUM ASSET SCANNER")
act = st.text_area("LISTA DE ACTIVOS (PROPIEDADES, AUTOS, YATES):")
if st.button("🧬 INICIAR ESCANEO"):
    with st.spinner("Escaneando..."):
        time.sleep(1.5)
        st.success("VALUACIÓN DETECTADA: $42,500,000 USD")

if st.sidebar.button("🔒 LOGOUT"):
    st.session_state.auth = False; st.rerun()
